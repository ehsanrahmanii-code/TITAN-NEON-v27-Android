"""Persistent, validated user settings (watchlist, scan interval, UI personalization)."""
from __future__ import annotations
import json
import os
import threading
import time

from app.config import DATA_DIR, DEFAULT_SYMBOLS, MAX_WATCHLIST, SCAN_INTERVAL_SEC, to_symbol, valid_symbol

_FILE = DATA_DIR / "settings.json"
_LOCK = threading.RLock()
_MAX_UI_BYTES = 60_000
_STATE: dict | None = None


def _defaults() -> dict:
    return {"watchlist": list(DEFAULT_SYMBOLS), "scan_sec": SCAN_INTERVAL_SEC, "ui": {}, "ts": 0}


def _atomic_write(path, text: str) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _load() -> dict:
    global _STATE
    if _STATE is None:
        st = _defaults()
        try:
            raw = json.loads(_FILE.read_text(encoding="utf-8"))
            if isinstance(raw, dict):
                st.update({k: raw[k] for k in st if k in raw})
        except Exception:                                    # noqa: BLE001
            pass
        _STATE = st
    return _STATE


def get() -> dict:
    with _LOCK:
        return json.loads(json.dumps(_load()))


def get_watchlist() -> list[str]:
    with _LOCK:
        wl = _load().get("watchlist") or DEFAULT_SYMBOLS
        return list(wl)


def get_scan_sec() -> int:
    with _LOCK:
        return int(_load().get("scan_sec") or SCAN_INTERVAL_SEC)


def update(patch: dict) -> dict:
    """Validate + merge. Unknown keys are ignored; invalid values raise ValueError."""
    if not isinstance(patch, dict):
        raise ValueError("object expected")
    with _LOCK:
        st = _load()
        if "watchlist" in patch:
            wl = []
            for x in patch["watchlist"] if isinstance(patch["watchlist"], list) else []:
                s = to_symbol(x)
                if not s.endswith("USDT") and s.isalnum():
                    s += "USDT"
                if valid_symbol(s) and s not in wl:
                    wl.append(s)
            if not wl:
                raise ValueError("watchlist empty/invalid")
            st["watchlist"] = wl[:MAX_WATCHLIST]
        if "scan_sec" in patch:
            st["scan_sec"] = max(30, min(900, int(patch["scan_sec"])))
        if "ui" in patch:
            ui = patch["ui"]
            if not isinstance(ui, dict) or len(json.dumps(ui)) > _MAX_UI_BYTES:
                raise ValueError("ui too large / invalid")
            st["ui"] = ui
        st["ts"] = time.time()
        _atomic_write(_FILE, json.dumps(st, ensure_ascii=False, indent=1))
        return json.loads(json.dumps(st))
