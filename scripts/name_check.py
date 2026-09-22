#!/usr/bin/env python3
"""name_check.py — checa disponibilidade de nome/handle de canal no YouTube.

Uso:
  python scripts/name_check.py "Cold File Diaries" "Arquivo Sombrio"
  python scripts/name_check.py --handle coldfilediaries --handle arquivosombrio

Requer OAuth (python scripts/yt_auth.py). Usa YouTube Data API v3 (leitura).
"""
import argparse
import sys
from pathlib import Path

TOKEN = Path.home() / ".config" / "opencode" / "secrets" / "yt-token.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]


def creds():
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    if not TOKEN.exists():
        print("[!] Rodric: python scripts/yt_auth.py")
        sys.exit(2)
    c = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not c.valid and c.expired and c.refresh_token:
        c.refresh(Request())
        TOKEN.write_text(c.to_json(), encoding="utf-8")
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("names", nargs="*", help="nomes de canal para checar")
    ap.add_argument("--handle", action="append", default=[], help="handle (sem @)")
    a = ap.parse_args()

    from googleapiclient.discovery import build
    yt = build("youtube", "v3", credentials=creds())

    for name in a.names:
        print(f"\n=== Nome: {name} ===")
        try:
            r = yt.search().list(part="snippet", q=name, type="channel", maxResults=8).execute()
            items = r.get("items", [])
            if not items:
                print("  nenhum canal encontrado com esse nome -> provavelmente disponivel")
            for it in items:
                t = it["snippet"]["title"]
                cid = it["snippet"]["channelId"]
                print(f"  - {t}  ({cid})")
        except Exception as e:  # noqa
            print(f"  [!] erro na busca: {e}")

    for h in a.handle:
        h = h.lstrip("@")
        print(f"\n=== Handle: @{h} ===")
        try:
            r = yt.channels().list(part="snippet,statistics", forHandle=h).execute()
            if r.get("items"):
                it = r["items"][0]
                st = it.get("statistics", {})
                print(f"  OCUPADO por: {it['snippet']['title']} | subs {st.get('subscriberCount','?')}")
            else:
                print("  LIVRE (nenhum canal com esse handle)")
        except Exception as e:  # noqa
            print(f"  [!] erro: {e}")

    print("\nObs.: 'livre' na API nao garante marca registrada. Cheque o INPI/EUIPO para uso comercial.")


if __name__ == "__main__":
    main()
