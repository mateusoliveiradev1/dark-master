#!/usr/bin/env python3
"""yt_db.py — camada de dados do dark-master."""
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
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


_load_env()
DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()


def backend():
    return "postgres" if DATABASE_URL else "sqlite"


def conn():
    if DATABASE_URL:
        try:
            import psycopg2
            c = psycopg2.connect(DATABASE_URL, connect_timeout=10)
            c.autocommit = False
            return c
        except Exception as exc:
            print(f"[!] Falha no Postgres ({exc}). Caindo para SQLite local.")
    SQLITE_DB.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(SQLITE_DB)
    c.row_factory = sqlite3.Row
    return c


def _is_postgres(c):
    return c.__class__.__module__.startswith("psycopg2")


def _q(c, sql):
    return sql.replace("?", "%s") if _is_postgres(c) else sql


def _exec(c, sql, params=()):
    cur = c.cursor()
    cur.execute(_q(c, sql), params)
    return cur


def _rows(c, sql, params=()):
    cur = c.cursor()
    cur.execute(_q(c, sql), params)
    cols = [d[0] for d in cur.description]
    out = []
    for row in cur.fetchall():
        if isinstance(row, dict):
            out.append(row)
        else:
            out.append({cols[i]: row[i] for i in range(len(cols))})
    return out


PG_SCHEMA = """
CREATE TABLE IF NOT EXISTS snapshots (
  id SERIAL PRIMARY KEY,
  ts TEXT NOT NULL, channel TEXT NOT NULL, video_id TEXT NOT NULL,
  title TEXT, format TEXT, published TEXT,
  views INTEGER, engaged_views INTEGER, avd_seconds DOUBLE PRECISION,
  avp_percent DOUBLE PRECISION, ctr_percent DOUBLE PRECISION,
  shown_in_feed INTEGER, chose_to_view_percent DOUBLE PRECISION,
  likes INTEGER, comments INTEGER, shares INTEGER, subscribers_gained INTEGER,
  subscribers_lost INTEGER, dislikes INTEGER,
  watch_hours DOUBLE PRECISION, revenue_usd DOUBLE PRECISION,
  impressions INTEGER, duration_seconds INTEGER,
  traffic_source TEXT, snapshot_date TEXT, period_start TEXT, period_end TEXT,
  match_status TEXT, notes TEXT, UNIQUE(ts, channel, video_id)
);
CREATE TABLE IF NOT EXISTS videos (
  id SERIAL PRIMARY KEY,
  channel TEXT NOT NULL, video_id TEXT NOT NULL,
  video_tag TEXT, title TEXT, format TEXT, case_name TEXT, series TEXT,
  scheduled_date TEXT, published_at TEXT, duration_seconds INTEGER,
  match_status TEXT, match_confidence DOUBLE PRECISION, updated_at TEXT,
  UNIQUE(channel, video_id)
);
CREATE TABLE IF NOT EXISTS traffic_sources (
  id SERIAL PRIMARY KEY,
  captured_ts TEXT NOT NULL, channel TEXT NOT NULL, video_id TEXT NOT NULL,
  source_type TEXT NOT NULL, source_detail TEXT,
  views INTEGER, engaged_views INTEGER, watch_hours DOUBLE PRECISION,
  period_start TEXT, period_end TEXT,
  UNIQUE(captured_ts, channel, video_id, source_type, source_detail)
);
CREATE TABLE IF NOT EXISTS retention_points (
  id SERIAL PRIMARY KEY,
  captured_ts TEXT NOT NULL, channel TEXT NOT NULL, video_id TEXT NOT NULL,
  elapsed_ratio DOUBLE PRECISION, audience_watch_ratio DOUBLE PRECISION,
  relative_retention DOUBLE PRECISION, period_start TEXT, period_end TEXT,
  UNIQUE(captured_ts, channel, video_id, elapsed_ratio)
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
CREATE TABLE IF NOT EXISTS experiments (
  id SERIAL PRIMARY KEY,
  ts TEXT NOT NULL, channel TEXT NOT NULL, video_id TEXT,
  scope TEXT, variable TEXT, hypothesis TEXT, baseline TEXT, target TEXT,
  start_date TEXT, end_date TEXT, status TEXT DEFAULT 'proposto',
  evidence TEXT, decision TEXT, UNIQUE(channel, start_date, variable)
);
CREATE INDEX IF NOT EXISTS idx_snap_video ON snapshots(channel, video_id);
CREATE INDEX IF NOT EXISTS idx_snap_ts ON snapshots(ts);
CREATE INDEX IF NOT EXISTS idx_video_tag ON videos(channel, video_tag, format);
CREATE INDEX IF NOT EXISTS idx_traffic_video ON traffic_sources(channel, video_id);
CREATE INDEX IF NOT EXISTS idx_retention_video ON retention_points(channel, video_id);
"""

TRAFFIC_MIGRATIONS = {"period_start": "TEXT", "period_end": "TEXT"}
RETENTION_MIGRATIONS = {"period_start": "TEXT", "period_end": "TEXT"}

SNAPSHOT_MIGRATIONS = {
    "dislikes": "INTEGER",
    "subscribers_lost": "INTEGER",
    "impressions": "INTEGER",
    "duration_seconds": "INTEGER",
    "snapshot_date": "TEXT",
    "period_start": "TEXT",
    "period_end": "TEXT",
    "match_status": "TEXT",
    "notes": "TEXT",
}

SQLITE_SCHEMA = PG_SCHEMA.replace("SERIAL PRIMARY KEY", "INTEGER PRIMARY KEY AUTOINCREMENT") \
    .replace("DOUBLE PRECISION", "REAL")


def _columns(c, table):
    if _is_postgres(c):
        rows = _rows(c, "SELECT column_name FROM information_schema.columns WHERE table_name=?", (table,))
        return {r["column_name"] for r in rows}
    return {r[1] for r in _rows(c, f"PRAGMA table_info({table})")}


def _migrate(c):
    existing = _columns(c, "snapshots")
    legacy_columns = {"subs_gained": "subscribers_gained", "subs_lost": "subscribers_lost"}
    for old, new in legacy_columns.items():
        if old in existing and new not in existing:
            _exec(c, f"ALTER TABLE snapshots RENAME COLUMN {old} TO {new}")
            existing.remove(old)
            existing.add(new)
        elif old in existing and new in existing:
            _exec(c, f"UPDATE snapshots SET {new}=COALESCE({new}, {old})")
    for name, sql_type in SNAPSHOT_MIGRATIONS.items():
        if name not in existing:
            _exec(c, f"ALTER TABLE snapshots ADD COLUMN {name} {sql_type}")
    for table, migrations in (("traffic_sources", TRAFFIC_MIGRATIONS), ("retention_points", RETENTION_MIGRATIONS)):
        table_columns = _columns(c, table)
        for name, sql_type in migrations.items():
            if name not in table_columns:
                _exec(c, f"ALTER TABLE {table} ADD COLUMN {name} {sql_type}")


def init(quiet=False):
    c = conn()
    postgres = _is_postgres(c)
    if postgres:
        lock = c.cursor()
        lock.execute("SELECT pg_advisory_lock(71420260923)")
    try:
        if postgres:
            for stmt in PG_SCHEMA.split(";"):
                if stmt.strip():
                    cur = c.cursor()
                    cur.execute(stmt)
        else:
            c.executescript(SQLITE_SCHEMA)
        _migrate(c)
        c.commit()
    except Exception:
        c.rollback()
        raise
    finally:
        if postgres:
            lock.execute("SELECT pg_advisory_unlock(71420260923)")
            lock.close()
        c.close()
    if not quiet:
        print(f"[OK] schema criado/atualizado | backend: {backend()}")


def save_snapshot(rec):
    c = conn()
    _exec(c, """INSERT INTO snapshots
        (ts,channel,video_id,title,format,published,views,engaged_views,avd_seconds,
         avp_percent,ctr_percent,shown_in_feed,chose_to_view_percent,likes,comments,
         shares,subscribers_gained,subscribers_lost,dislikes,watch_hours,revenue_usd,
         impressions,duration_seconds,traffic_source,snapshot_date,period_start,period_end,
         match_status,notes)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(ts,channel,video_id) DO UPDATE SET
          title=excluded.title, format=excluded.format, published=excluded.published,
          views=excluded.views, engaged_views=excluded.engaged_views,
          avd_seconds=excluded.avd_seconds, avp_percent=excluded.avp_percent,
          ctr_percent=excluded.ctr_percent, shown_in_feed=excluded.shown_in_feed,
          chose_to_view_percent=excluded.chose_to_view_percent, likes=excluded.likes,
          comments=excluded.comments, shares=excluded.shares,
          subscribers_gained=excluded.subscribers_gained,
          subscribers_lost=excluded.subscribers_lost, dislikes=excluded.dislikes,
          watch_hours=excluded.watch_hours, revenue_usd=excluded.revenue_usd,
          impressions=excluded.impressions, duration_seconds=excluded.duration_seconds,
          traffic_source=excluded.traffic_source, snapshot_date=excluded.snapshot_date,
          period_start=excluded.period_start, period_end=excluded.period_end,
          match_status=excluded.match_status, notes=excluded.notes""",
        (rec.get("ts"), rec.get("channel"), rec.get("video_id"), rec.get("title"),
         rec.get("format"), rec.get("published"), rec.get("views"), rec.get("engaged_views"),
         rec.get("avd_seconds"), rec.get("avp_percent"), rec.get("ctr_percent"),
         rec.get("shown_in_feed"), rec.get("chose_to_view_percent"), rec.get("likes"),
         rec.get("comments"), rec.get("shares"), rec.get("subscribers_gained"),
         rec.get("subscribers_lost"), rec.get("dislikes"), rec.get("watch_hours"),
         rec.get("revenue_usd"), rec.get("impressions"), rec.get("duration_seconds"),
         rec.get("traffic_source"), rec.get("snapshot_date"), rec.get("period_start"),
         rec.get("period_end"), rec.get("match_status"), rec.get("notes")))
    c.commit()
    c.close()


def save_video(rec):
    c = conn()
    _exec(c, """INSERT INTO videos
        (channel,video_id,video_tag,title,format,case_name,series,scheduled_date,
         published_at,duration_seconds,match_status,match_confidence,updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(channel,video_id) DO UPDATE SET
          video_tag=excluded.video_tag, title=excluded.title, format=excluded.format,
          case_name=excluded.case_name, series=excluded.series,
          scheduled_date=excluded.scheduled_date, published_at=excluded.published_at,
          duration_seconds=excluded.duration_seconds, match_status=excluded.match_status,
          match_confidence=excluded.match_confidence, updated_at=excluded.updated_at""",
        (rec.get("channel"), rec.get("video_id"), rec.get("video_tag"), rec.get("title"),
         rec.get("format"), rec.get("case_name"), rec.get("series"), rec.get("scheduled_date"),
         rec.get("published_at"), rec.get("duration_seconds"), rec.get("match_status"),
         rec.get("match_confidence"), rec.get("updated_at") or datetime.now().isoformat(timespec="seconds")))
    c.commit()
    c.close()


def save_traffic_source(rec):
    c = conn()
    _exec(c, """INSERT INTO traffic_sources
        (captured_ts,channel,video_id,source_type,source_detail,views,engaged_views,watch_hours,period_start,period_end)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(captured_ts,channel,video_id,source_type,source_detail) DO UPDATE SET
          views=excluded.views, engaged_views=excluded.engaged_views,
          watch_hours=excluded.watch_hours, period_start=excluded.period_start,
          period_end=excluded.period_end""",
        (rec.get("captured_ts"), rec.get("channel"), rec.get("video_id"),
         rec.get("source_type"), rec.get("source_detail") or "", rec.get("views"),
         rec.get("engaged_views"), rec.get("watch_hours"), rec.get("period_start"), rec.get("period_end")))
    c.commit()
    c.close()


def save_retention(rec):
    c = conn()
    _exec(c, """INSERT INTO retention_points
        (captured_ts,channel,video_id,elapsed_ratio,audience_watch_ratio,relative_retention,period_start,period_end)
        VALUES (?,?,?,?,?,?,?,?)
        ON CONFLICT(captured_ts,channel,video_id,elapsed_ratio) DO UPDATE SET
          audience_watch_ratio=excluded.audience_watch_ratio,
          relative_retention=excluded.relative_retention, period_start=excluded.period_start,
          period_end=excluded.period_end""",
        (rec.get("captured_ts"), rec.get("channel"), rec.get("video_id"),
         rec.get("elapsed_ratio"), rec.get("audience_watch_ratio"),
         rec.get("relative_retention"), rec.get("period_start"), rec.get("period_end")))
    c.commit()
    c.close()


def compact_capture(channel, captured_ts, period_start, period_end):
    c = conn()
    for table in ("snapshots", "traffic_sources", "retention_points"):
        _exec(c, f"""DELETE FROM {table}
            WHERE channel=? AND period_start=? AND period_end=? AND {('ts' if table == 'snapshots' else 'captured_ts')}<>?""",
              (channel, period_start, period_end, captured_ts))
    c.commit()
    c.close()


def save_outlier(rec):
    c = conn()
    _exec(c, """INSERT INTO outliers
        (detected_ts,channel,video_id,title,format,views,channel_median,ratio,pattern,note)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(detected_ts,channel,video_id) DO UPDATE SET
          views=excluded.views, channel_median=excluded.channel_median,
          ratio=excluded.ratio, title=excluded.title, pattern=excluded.pattern,
          note=excluded.note""",
        (rec.get("detected_ts"), rec.get("channel"), rec.get("video_id"), rec.get("title"),
         rec.get("format"), rec.get("views"), rec.get("channel_median"), rec.get("ratio"),
         rec.get("pattern"), rec.get("note")))
    c.commit()
    c.close()


def add_learning(finding, evidence="", decision="", channel=None, status="proposto"):
    c = conn()
    _exec(c, "INSERT INTO learnings (ts,channel,finding,evidence,decision,status) VALUES (?,?,?,?,?,?)",
          (datetime.now().isoformat(timespec="seconds"), channel, finding, evidence, decision, status))
    c.commit()
    c.close()


def save_experiment(rec):
    c = conn()
    _exec(c, """INSERT INTO experiments
        (ts,channel,video_id,scope,variable,hypothesis,baseline,target,start_date,end_date,
         status,evidence,decision)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(channel,start_date,variable) DO UPDATE SET
          video_id=excluded.video_id, scope=excluded.scope, hypothesis=excluded.hypothesis,
          baseline=excluded.baseline, target=excluded.target, end_date=excluded.end_date,
          status=excluded.status, evidence=excluded.evidence, decision=excluded.decision""",
        (rec.get("ts") or datetime.now().isoformat(timespec="seconds"), rec.get("channel"),
         rec.get("video_id"), rec.get("scope"), rec.get("variable"), rec.get("hypothesis"),
         rec.get("baseline"), rec.get("target"), rec.get("start_date"), rec.get("end_date"),
         rec.get("status") or "proposto", rec.get("evidence"), rec.get("decision")))
    c.commit()
    c.close()


def stats():
    try:
        c = conn()
    except Exception as exc:
        print(f"[!] sem conexão: {exc}")
        return
    for table in ("snapshots", "videos", "traffic_sources", "retention_points", "outliers", "learnings", "experiments"):
        try:
            count = _rows(c, f"SELECT COUNT(*) AS n FROM {table}")[0]["n"]
        except Exception:
            count = "erro de migração"
        print(f"{table}: {count} linha(s)")
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
        print("[OK] conexão funcionando")
    except Exception as exc:
        print(f"[!] erro: {exc}")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "init"
    {"init": init, "stats": stats, "doctor": doctor}.get(command, init)()
