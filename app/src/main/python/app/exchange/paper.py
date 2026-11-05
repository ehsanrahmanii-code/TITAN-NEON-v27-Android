"""Paper exchange stub."""
from __future__ import annotations
_account = {"equity": 10000.0, "cash": 10000.0, "open_positions": [], "closed": [], "auto": False}

def get_account(prices=None):
    return dict(_account)

def open_position(*a, **k):
    return {"ok": False, "error": "paper module loading"}

def close_position(pid, price):
    return {"ok": False, "error": "not found"}

def set_auto_trade(enabled):
    _account["auto"] = bool(enabled)
    return {"ok": True, "auto": _account["auto"]}

def reset_account():
    _account.update({"equity": 10000.0, "cash": 10000.0, "open_positions": [], "closed": []})
    return {"ok": True}
