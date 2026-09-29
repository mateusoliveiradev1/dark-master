#!/usr/bin/env python3
"""yt_secrets.py — resolve qual token OAuth usar (multi-conta).

1 token = 1 conta Google. Canais na mesma conta usam o token padrao
(`yt-token.json`); canal de outra conta usa `yt-token-<alias>.json`,
criado com `python scripts/yt_auth.py --account <alias>`.

Ordem: --account/argumento > env YT_ACCOUNT > padrao.
"""
import os
import re
from pathlib import Path

SECRETS = Path.home() / ".config" / "opencode" / "secrets"


def token_path(account=None):
    account = (account or os.environ.get("YT_ACCOUNT", "") or "").strip()
    if account:
        safe = re.sub(r"\W+", "", account)
        return SECRETS / f"yt-token-{safe}.json"
    return SECRETS / "yt-token.json"
