import string
import random
from src.strong_password_generator.sqlite import create_connection
from datetime import date

class Password:
    def create_password(self, site, url, email) -> None:
        today = date.today()
        strong_password = self.generate_password()

        conn = create_connection()
        with conn:
            password = (site, url, email, strong_password, today.strftime("%Y-%m-%d"))

            sql = """ INSERT INTO passwords(site_name, site_url, email, password, created_at)
                VALUES(?, ?, ?, ?, ?) """

            cur = conn.cursor()
            cur.execute(sql, password)
            conn.commit()

        return strong_password

    def search_password(self, value) -> None:
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM passwords WHERE site_name LIKE ? or site_url LIKE ?", (f"%{value}%", f"%{value}%"))

            rows = cur.fetchall()

        return rows

    def generate_password(self, size=16) -> str:
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(size))