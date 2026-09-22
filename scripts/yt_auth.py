#!/usr/bin/env python3
"""yt_auth.py — faz o OAuth do YouTube e salva o token.

Uso:
  1) Baixe o OAuth Client ID (Desktop app) como client_secrets.json e coloque em:
       C:\\Users\\Liiiraa\\.config\\opencode\\secrets\\client_secrets.json
  2) Rode:  python scripts/yt_auth.py
     (abre o navegador; autorize; o token fica salvo em secrets/yt-token.json)

Escopos: youtube.readonly + yt-analytics.readonly + yt-analytics-monetary.readonly
"""
import os
import sys
from pathlib import Path

SECRETS = Path.home() / ".config" / "opencode" / "secrets"
CLIENT = SECRETS / "client_secrets.json"
TOKEN = SECRETS / "yt-token.json"

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/yt-analytics.readonly",
    "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",
]


def main():
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print("Instale as libs: python -m pip install google-api-python-client google-auth-oauthlib")
        sys.exit(1)

    SECRETS.mkdir(parents=True, exist_ok=True)
    if not CLIENT.exists():
        print(f"[!] client_secrets.json nao encontrado em:\n    {CLIENT}")
        print("\nComo criar (Google Cloud Console):")
        print("  1. https://console.cloud.google.com/ -> criar projeto")
        print("  2. APIs e servicos > Biblioteca > habilitar 'YouTube Data API v3' e 'YouTube Analytics API'")
        print("  3. APIs e servicos > Credenciais > Criar credenciais > ID do cliente OAuth")
        print("     Tipo de aplicativo: Aplicativo para computador (Desktop app)")
        print("  4. Baixar o JSON e salvar como: " + str(CLIENT))
        sys.exit(2)

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT), SCOPES)
    print("Abrindo o navegador para autorizar... (faca login e clique em Permitir)")
    creds = flow.run_local_server(port=0, prompt="consent", access_type="offline")

    TOKEN.write_text(creds.to_json(), encoding="utf-8")
    print(f"[OK] Token salvo em: {TOKEN}")
    print("Agora rode: python scripts/yt_metrics.py")


if __name__ == "__main__":
    main()
