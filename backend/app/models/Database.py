import psycopg2
import os
import time

class Database():
    def __init__(self):
        while True:
            try:
                self.conn = psycopg2.connect(
                    host = os.getenv('DB_HOST'),
                    database = os.getenv('DB_NAME'),
                    user = os.getenv('DB_USER'),
                    password = os.getenv('DB_PASS')
                )
                break
            except Exception as e:
                time.sleep(3)
                continue
        self.cur = self.conn.cursor()

    def query(self, query, *args):
        self.cur.execute(query, args)
        return self.cur.fetchall()
    
    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

    def test(self):
        self.query('SELECT 123 FROM users')
        return self.cur.fetchall()