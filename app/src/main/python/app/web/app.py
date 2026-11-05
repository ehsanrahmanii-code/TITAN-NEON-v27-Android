"""TITAN PRO NEON — Flask API + dashboard (Android build)."""
from __future__ import annotations
from flask import Flask, jsonify, request, render_template
from app.config import HOST, PORT, VERSION, TIMEFRAMES, DATA_DIR, to_symbol, valid_symbol
from app import settings

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["JSON_AS_ASCII"] = False
app.json.ensure_ascii = False

@app.route("/")
def index():
    try:
        return render_template("index.html", version=VERSION)
    except Exception:
        return f"<h1>Titan Neon {VERSION}</h1><p>Server running. Data: {DATA_DIR}</p>"

@app.route("/api/status")
def api_status():
    return jsonify({"version": VERSION, "timeframes": TIMEFRAMES, "symbols": settings.get_watchlist(),
                    "data_dir": str(DATA_DIR), "ok": True})

@app.route("/api/matrix")
def api_matrix():
    return jsonify({"ok": True, "signals": [], "message": "full modules loading..."})

def main():
    from waitress import serve
    print(f"TITAN PRO NEON {VERSION} → http://{HOST}:{PORT}   data: {DATA_DIR}")
    serve(app, host=HOST, port=PORT, threads=8)

if __name__ == "__main__":
    main()
