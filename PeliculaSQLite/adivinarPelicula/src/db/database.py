import sqlite3

class ScoreDatabase:
    def __init__(self, db_name="scores.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                score INTEGER
            )
        """)
        self.conn.commit()

    def add_score(self, username, score):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO scores (username, score) VALUES (?, ?)", (username, score))
        self.conn.commit()

    def get_scores(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT username, score FROM scores ORDER BY score DESC")
        return cursor.fetchall()

    def close(self):
        self.conn.close()