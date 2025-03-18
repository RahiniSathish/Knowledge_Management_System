import sqlite3
from contextlib import contextmanager

DB_NAME = "knowledge.db"

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
    finally:
        conn.close()

def setup_database():
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Create knowledge table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            createdtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            etc TEXT
        );
        ''')

        # Create document table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS document (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            knowledge_id INTEGER,
            filename TEXT NOT NULL,
            content TEXT NOT NULL,
            createdtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(knowledge_id) REFERENCES knowledge(id)
        );
        ''')

        conn.commit()

if __name__ == "__main__":
    setup_database()