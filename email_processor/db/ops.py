# email_processor/db/ops.py

import sqlite3

DATABASE_PATH = "email_data.db"

def init_db():
    """Initialize the database and create tables if they don't exist."""
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails(
            id INTEGER PRIMARY KEY,
            token TEXT NOT NULL,
            email_address TEXT NOT NULL,
            content TEXT
        );
        """)
        conn.commit()

def store_email_data(token, email_address, content):
    """Store the email's token, address, and content."""
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO emails (token, email_address, content)
        VALUES (?, ?, ?);
        """, (token, email_address, content))
        conn.commit()

def retrieve_email_by_token(token):
    """Retrieve the email address and content using a token."""
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT email_address, content FROM emails WHERE token=?", (token,))
        result = cursor.fetchone()
    return result if result else None
