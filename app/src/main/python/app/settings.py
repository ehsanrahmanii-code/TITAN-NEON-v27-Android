"""Persistent, validated user settings (watchlist, scan interval, UI personalization)."""
from __future__ import annotations
import json
import os
import threading
import time

from app.config import DATA_DIR, DEFAULT_SYMBOLS, MAX_WATCHLIST, SCAN_INTERVAL_SEC, to_symbol, valid_symbol

_FILE = DATA_DIR / "settings.json"
_lock = threading.RLock()
_cache: dict | None = None

_DEFAULTS = {
    "watchlist": list(DEFAULT_SYMBOLS),
    "scan_sec": SCAN_INTERVAL_SEC,
    "theme": "aurora",
    "shell": "panels",
    "perf": "auto",
    "lang": "fa",
    "auto_trade": False,
    "auto_mode": "balanced",
    "risk_pct": 1.0,
    "leverage": 10,
    "notes": {},
}


def _load() -> dict:
    global _cache
    with _lock:
        if _cache is not None:
            return dict(_cache)
        data = dict(_DEFAULTS)
        try:
            if _FILE.exists():
                raw = json.loads(_FILE.read_text(encoding="utf-8"))
                if isinstance(raw, dict):
                    data.update(raw)
        except Exception:
            pass
        wl = data.get("watchlist") or []
        cleaned = []
        for s in wl:
            s = to_symbol(s)
            if valid_symbol(s) and s not in cleaned:
                cleaned.append(s)
        if not cleaned:
            cleaned = list(DEFAULT_SYMBOLS)
        data["watchlist"] = cleaned[:MAX_WATCHLIST]
        data["scan_sec"] = max(30, min(600, int(data.get("scan_sec") or SCAN_INTERVAL_SEC)))
        _cache = data
        return dict(data)


def _save(data: dict) -> None:
    global _cache
    with _lock:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        tmp = _FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(_FILE)
        _cache = dict(data)


def get() -> dict:
    return _load()


def get_watchlist() -> list[str]:
    return list(_load().get("watchlist") or DEFAULT_SYMBOLS)


def get_scan_sec() -> int:
    return int(_load().get("scan_sec") or SCAN_INTERVAL_SEC)


def update(patch: dict) -> dict:
    data = _load()
    if "watchlist" in patch:
        wl = []
        for s in patch["watchlist"] or []:
            s = to_symbol(s)
            if valid_symbol(s) and s not in wl:
                wl.append(s)
        data["watchlist"] = wl[:MAX_WATCHLIST] or list(DEFAULT_SYMBOLS)
    for k in ("theme", "shell", "perf", "lang", "auto_mode"):
        if k in patch and patch[k] is not None:
            data[k] = str(patch[k])[:32]
    if "scan_sec" in patch:
        data["scan_sec"] = max(30, min(600, int(patch["scan_sec"])))
    if "auto_trade" in patch:
        data["auto_trade"] = bool(patch["auto_trade"])
    if "risk_pct" in patch:
        data["risk_pct"] = max(0.1, min(5.0, float(patch["risk_pct"])))
    if "leverage" in patch:
        data["leverage"] = max(1, min(50, int(patch["leverage"])))
    if "notes" in patch and isinstance(patch["notes"], dict):
        data["notes"] = {str(k)[:16]: str(v)[:500] for k, v in list(patch["notes"].items())[:40]}
    _save(data)
    return data
