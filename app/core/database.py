import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "activity.db"

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            process_name TEXT,
            window_title TEXT,
            duration INTEGER
        )
    """)

    conn.commit()
    conn.close()
