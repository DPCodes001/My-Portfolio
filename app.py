from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "portfolio.db")

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# -------- PUBLIC ROUTE --------
@app.route("/data", methods=["GET"])
def get_data():
    db = get_db()

    # TODO 1:
    # fetch ALL rows from the "content" table
    rows = db.execute("SELECT * FROM content").fetchall()

    # TODO 2:
    # convert rows into a list of dictionaries
    data = [dict(row) for row in rows]

    return jsonify(data)


# -------- ADMIN ROUTE --------
@app.route("/update", methods=["POST"])
def update_data():
    body = request.json

    # TODO 3:
    # read "key" and "value" from body
    key = body["key"]
    value = body["value"]

    db = get_db()

    # TODO 4:
    # update the content table where key matches
    db.execute(
        "UPDATE content SET value = ? WHERE key = ?",
        (value, key)
    )

    db.commit()
    return jsonify({"status": "updated"})


if __name__ == "__main__":
    app.run(debug=True)
