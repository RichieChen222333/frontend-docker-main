import os
import pymysql
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "demo")
DB_PASSWORD = os.getenv("DB_PASSWORD", "demo1234")
DB_NAME = os.getenv("DB_NAME", "demo_db")


def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.get("/api/health")
def health():
    return jsonify({"ok": True})


@app.get("/api/db-time")
def db_time():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW() AS now")
            row = cur.fetchone()
        return jsonify(row)
    finally:
        conn.close()
