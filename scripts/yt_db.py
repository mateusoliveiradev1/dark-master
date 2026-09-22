#!/usr/bin/env python3
"""yt_db.py — camada de dados do dark-master.

Usa Neon Postgres se DATABASE_URL estiver definida (env ou secrets/dark.env);
senao, cai para SQLite local (data/dark.db). API agnostica de backend.

Uso:
  python scripts/yt_db.py init      # cria/migra tabelas
  python scripts/yt_db.py stats     # resumo
  python scripts/yt_db.py doctor    # testa a conexao e mostra o backend ativo
"""
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SQLITE_DB = ROOT / "data" / "dark.db"
ENV_FILE = Path.home() / ".config" / "opencode" / "secrets" / "dark.env"


def _load_env():
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


_load_env()
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()


def backend():
    return "postgres" if DATABASE_URL else "sqlite"


# ---------- conexao ----------
def conn():
    if DATABASE_URL:
        try:
            import psycopg2
            import psycopg2.extras
            c = psycopg2.connect(DATABASE_URL, connect_timeout=10)
            c.autocommit = False
            return c
        except Exception as e:  # noqa
            print(f"[!] Falha no Postgres ({e}). Caindo para SQLite local.")
    SQLITE_DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(SQLITE_DB)
    c.row_factory = sqlite3.Row
    return c


def _q(sql):
    """Converte placeholders ?: para %s no Postgres."""
    return sql.replace("?", "%s") if DATABASE_URL else sql


def _exec(c, sql, params=()):
    cur = c.cursor()
    cur.execute(_q(sql), params)


def _rows(c, sql, params=()):
    cur = c.cursor()
    cur.execute(_q(sql), params)
    cols = [d[0] for d in cur.description]
    out = []
    for r in cur.fetchall():
        if isinstance(r, dict):
            out.append(r)
        else:
            out.append({cols[i]: r[i] for i in range(len(cols))})
    return out


# ---------- schema ----------
PG_SCHEMA = """
CREATE TABLE IF NOT EXISTS snapshots (
  id SERIAL PRIMARY KEY,
  ts TEXT NOT NULL, channel TEXT NOT NULL, video_id TEXT NOT NULL,
  title TEXT, format TEXT, published TEXT,
  views INTEGER, engaged_views INTEGER, avd_seconds DOUBLE PRECISION,
  avp_percent DOUBLE PRECISION, ctr_percent DOUBLE PRECISION,
  shown_in_feed INTEGER, chose_to_view_percent DOUBLE PRECISION,
  likes INTEGER, comments INTEGER, shares INTEGER, subs_gained INTEGER,
  watch_hours DOUBLE PRECISION, revenue_usd DOUBLE PRECISION,
  traffic_source TEXT, UNIQUE(ts, channel, video_id)
);
CREATE TABLE IF NOT EXISTS outliers (
  id SERIAL PRIMARY KEY,
  detected_ts TEXT NOT NULL, channel TEXT NOT NULL, video_id TEXT NOT NULL,
  title TEXT, format TEXT, views INTEGER, channel_median DOUBLE PRECISION,
  ratio DOUBLE PRECISION, pattern TEXT, note TEXT,
  UNIQUE(detected_ts, channel, video_id)
);
CREATE TABLE IF NOT EXISTS learnings (
  id SERIAL PRIMARY KEY,
  ts TEXT NOT NULL, channel TEXT, finding TEXT NOT NULL, evidence TEXT,
  decision TEXT, status TEXT DEFAULT 'proposto'
);
CREATE INDEX IF NOT EXISTS idx_snap_video ON snapshots(channel, video_id);
CREATE INDEX IF NOT EXISTS idx_snap_ts ON snapshots(ts);
"""

SQLITE_SCHEMA = PG_SCHEMA.replace("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") \
    .replace("DOUBLE PRECISION", "REAL")


def init():
    c = conn()
    if DATABASE_URL:
        cur = c.cursor()
        for stmt in PG_SCHEMA.split(";"):
            if stmt.strip():
                cur.execute(stmt)
        c.commit()
    else:
        c.executescript(SQLITE_SCHEMA)
        c.commit()
    c.close()
    print(f"[OK] schema criado/atualizado | backend: {backend()}")


# ---------- writers (usados pelos outros scripts) ----------
def save_snapshot(rec: dict):
    c = conn()
    _exec(c, """INSERT INTO snapshots
        (ts,channel,video_id,title,format,published,views,engaged_views,avd_seconds,
         avp_percent,ctr_percent,shown_in_feed,chose_to_view_percent,likes,comments,
         shares,subs_gained,watch_hours,revenue_usd,traffic_source)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT (ts,channel,video_id) DO UPDATE SET
          views=excluded.views, engaged_views=excluded.engaged_views,
          avd_seconds=excluded.avd_seconds, avp_percent=excluded.avp_percent,
          watch_hours=excluded.watch_hours, likes=excluded.likes,
          comments=excluded.comments, shares=excluded.shares,
          subs_gained=excluded.subs_gained""",
        (rec.get("ts"), rec.get("channel"), rec.get("video_id"), rec.get("title"),
         rec.get("format"), rec.get("published"), rec.get("views"), rec.get("engaged_views"),
         rec.get("avd_seconds"), rec.get("avp_percent"), rec.get("ctr_percent"),
         rec.get("shown_in_feed"), rec.get("chose_to_view_percent"), rec.get("likes"),
         rec.get("comments"), rec.get("shares"), rec.get("subs_gained"),
         rec.get("watch_hours"), rec.get("revenue_usd"), rec.get("traffic_source")))
    c.commit()
    c.close()


def save_outlier(rec: dict):
    c = conn()
    _exec(c, """INSERT INTO outliers
        (detected_ts,channel,video_id,title,format,views,channel_median,ratio,pattern,note)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT (detected_ts,channel,video_id) DO UPDATE SET
          views=excluded.views, channel_median=excluded.channel_median,
          ratio=excluded.ratio, title=excluded.title""",
        (rec.get("detected_ts"), rec.get("channel"), rec.get("video_id"), rec.get("title"),
         rec.get("format"), rec.get("views"), rec.get("channel_median"), rec.get("ratio"),
         rec.get("pattern"), rec.get("note")))
    c.commit()
    c.close()


def add_learning(finding, evidence="", decision="", channel=None, status="proposto"):
    c = conn()
    _exec(c, """INSERT INTO learnings (ts,channel,finding,evidence,decision,status)
        VALUES (?,?,?,?,?,?)""",
        (datetime.now().isoformat(timespec="seconds"), channel, finding, evidence, decision, status))
    c.commit()
    c.close()


# ---------- util ----------
def stats():
    try:
        c = conn()
    except Exception as e:  # noqa
        print(f"[!] sem conexao: {e}")
        return
    for t in ("snapshots", "outliers", "learnings"):
        n = _rows(c, f"SELECT COUNT(*) AS n FROM {t}")[0]["n"]
        print(f"{t}: {n} linha(s)")
    c.close()
    print(f"backend: {backend()}")


def doctor():
    print(f"backend configurado: {backend()}")
    if DATABASE_URL:
        safe = DATABASE_URL.split("@")[-1] if "@" in DATABASE_URL else "(url)"
        print(f"host: ...@{safe}")
    try:
        init()
        stats()
        print("[OK] conexao funcionando")
    except Exception as e:  # noqa
        print(f"[!] erro: {e}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "init"
    {"init": init, "stats": stats, "doctor": doctor}.get(cmd, init)()
