"""Market data stubs for Android build."""
from __future__ import annotations
import pandas as pd
from datetime import datetime, timezone

def fetch_klines(symbol, tf="1h", limit=300):
    now = int(datetime.now(timezone.utc).timestamp()*1000)
    rows = [{"open_time": datetime.fromtimestamp((now - i*3600000)/1000, tz=timezone.utc),
             "open":100.0,"high":101.0,"low":99.0,"close":100.5,"volume":1.0} for i in range(limit,0,-1)]
    return pd.DataFrame(rows)

def closed_only(df, tf):
    return df.iloc[:-1] if len(df)>1 else df

def fetch_prices(symbols):
    return {s: 100.0 for s in symbols}

def fetch_ticker(symbol):
    return {"symbol": symbol, "price": 100.0, "change_pct": 0.0}

def fetch_depth(symbol):
    return {"bids": [], "asks": []}

def fetch_derivs(symbol):
    return {}
