from pathlib import Path

from flask import Flask, send_from_directory


BASE_DIR = Path(__file__).resolve().parent

app = Flask(
    __name__,
    static_folder="",
    template_folder="",
)


@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/<path:path>")
def static_proxy(path: str):
    return send_from_directory(BASE_DIR, path)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

