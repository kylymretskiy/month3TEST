import sqlite3


class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_product TEXT,
                    category TEXT,
                    size TEXT,
                    price INTEGER,
                    product_id INTEGER,
                    photo TEXT
                )
            """)
            conn.commit()
    def add_complaint(self, data: dict):
        print(data)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO products (name_product,category, price, size ,product_id,photo)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (data["name_product"],data["category"] ,data["price"], data["size"], data["product_id"], data["photo"]),
            )
            conn.commit()


def get_db_connection():
    conn = sqlite3.connect('db/products.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return products
