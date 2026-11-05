"""Lightweight evidence / why-opened helpers for auto-trade decisions."""
from __future__ import annotations
from typing import Any


def summarize(decision: dict) -> dict:
    """Turn internal decision dict into a short human-readable evidence block."""
    reasons = decision.get("reasons") or decision.get("why") or []
    if isinstance(reasons, str):
        reasons = [reasons]
    blocked = decision.get("blocked") or decision.get("blockers") or []
    if isinstance(blocked, str):
        blocked = [blocked]
    return {
        "ok": bool(decision.get("ok", decision.get("open", False))),
        "side": decision.get("side") or decision.get("action") or "WAIT",
        "score": float(decision.get("score") or decision.get("conf") or 0),
        "reasons": [str(r)[:120] for r in reasons][:12],
        "blocked": [str(b)[:120] for b in blocked][:12],
        "symbol": decision.get("symbol"),
        "tf": decision.get("tf"),
    }
