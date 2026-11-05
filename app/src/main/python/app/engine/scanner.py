"""Scanner stub."""
from __future__ import annotations
import threading, time

_status = {"running": False, "progress": 0, "last": 0}

def get_status():
    return dict(_status)

def get_matrix():
    return {"signals": [], "updated": time.time()}

def start_scan(syms=None, tfs=None):
    return {"ok": True, "started": True}

def start_background():
    def _loop():
        while True:
            time.sleep(90)
    t = threading.Thread(target=_loop, daemon=True)
    t.start()
