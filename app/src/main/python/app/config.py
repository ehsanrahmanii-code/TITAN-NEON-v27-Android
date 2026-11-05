"""TITAN PRO NEON — configuration (every path/limit can be overridden by env)."""
from __future__ import annotations
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.getenv("TITAN_DATA", str(ROOT / "VVV"))).expanduser()
TTT_DIR = DATA_DIR                      # legacy alias — all cache/memory/data ONLY in UUU/VVV
SECRET_DIR = Path(os.getenv("TITAN_SECRET", str(ROOT / "secret"))).expanduser()
for _d in (DATA_DIR, SECRET_DIR):
    _d.mkdir(parents=True, exist_ok=True)

HOST = os.getenv("TITAN_HOST", "127.0.0.1")
PORT = int(os.getenv("TITAN_PORT", "8080"))
VERSION = "2.7.3-FULL-THEME"

DEFAULT_COINS = [
    "BTC/USDT", "ETH/USDT", "BNB/USDT", "XRP/USDT", "SOL/USDT",
    "ADA/USDT", "DOGE/USDT", "AVAX/USDT", "LINK/USDT", "NEAR/USDT",
    "SUI/USDT", "TAO/USDT", "AAVE/USDT", "BCH/USDT", "XLM/USDT",
    "TRX/USDT", "SHIB/USDT", "PEPE/USDT", "WIF/USDT", "FLOKI/USDT",
    "CAKE/USDT", "HYPE/USDT", "ZEC/USDT", "XAUT/USDT",
]
SYMBOL_RE = re.compile(r"^[A-Z0-9]{2,14}USDT$")


def to_symbol(coin: str) -> str:
    return str(coin).replace("/", "").replace("-", "").strip().upper()


def to_base(coin: str) -> str:
    c = str(coin).upper()
    if "/" in c:
        return c.split("/")[0]
    return c[:-4] if c.endswith("USDT") else c


def valid_symbol(sym: str) -> bool:
    return bool(SYMBOL_RE.match(to_symbol(sym)))


DEFAULT_SYMBOLS = [to_symbol(c) for c in DEFAULT_COINS]
MAX_WATCHLIST = 40
TIMEFRAMES = ["15m", "1h", "4h", "1d"]
TF_PRIORITY = ["1h", "4h", "1d", "15m"]          # scan order (most useful first)
TF_WEIGHT = {"15m": 0.15, "1h": 0.25, "4h": 0.30, "1d": 0.30}
KLINE_LIMIT = 300                                  # EMA200 needs real warm-up
CHART_KLINES = 300
FORECAST_CANDLES = 32
MC_PATHS = 600

SCAN_INTERVAL_SEC = int(os.getenv("TITAN_SCAN_SEC", "90"))
CPU_WORKERS = int(os.getenv("TITAN_CPU_WORKERS", "6"))

# Signal thresholds (slightly lower to capture more high-quality continuations without flooding WAIT→signal)
SIDE_THRESHOLD = 34.0

# Paper exchange
STARTING_CAPITAL = 10_000.0
DEFAULT_LEVERAGE = 10
MAX_LEVERAGE = 50
FEE_TAKER = 0.0004
FEE_MAKER = 0.0002
SLIPPAGE = 0.0002
MAX_OPEN_POSITIONS = 12
RISK_PER_TRADE_PCT = 1.0
MAX_MARGIN_PCT_PER_POS = 20.0     # of equity
MAX_TOTAL_MARGIN_PCT = 60.0       # of equity
DAILY_LOSS_LIMIT_PCT = 8.0
PARTIALS = (0.40, 0.35, 0.25)     # TP1 / TP2 / TP3 close fractions
AUTO_MIN_CONF = 0.52
AUTO_MIN_RR = 1.45
AUTO_COOLDOWN_SEC = 2 * 3600      # after a losing auto trade on the same coin

# AI
GEMINI_MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
AI_TIMEOUT_SEC = 18
