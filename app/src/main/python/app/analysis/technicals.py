"""Technicals stub."""
from __future__ import annotations
from dataclasses import dataclass, asdict

@dataclass
class Signal:
    symbol: str = ""
    tf: str = "1h"
    side: str = "WAIT"
    score: float = 0.0
    entry: float = 0.0
    stop: float = 0.0
    tp1: float = 0.0
    tp2: float = 0.0
    tp3: float = 0.0
    def to_dict(self):
        return asdict(self)

def analyze(df, symbol, tf, price=None):
    return Signal(symbol=symbol, tf=tf, side="WAIT")
