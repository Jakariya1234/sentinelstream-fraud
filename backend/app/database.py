import sqlite3, csv, os

DB_NAME = "transactions.db"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_FILE = os.path.join(BASE_DIR, "sample_transactions.csv")

def load_csv():
    data = set()
    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for r in reader:
            data.add((
                r["transaction_id"],
                float(r["amount"]),
                r["merchant"],
                r["location"]
            ))
    return data

CSV_DATA = load_csv()

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_id TEXT,
            amount REAL,
            merchant TEXT,
            location TEXT,
            risk_score REAL,
            decision TEXT
        )"""
    )
    conn.commit()
    conn.close()

def save_transaction(txn, risk, decision):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (transaction_id, amount, merchant, location, risk_score, decision) VALUES (?,?,?,?,?,?)",
        (txn.transaction_id, txn.amount, txn.merchant, txn.location, risk, decision)
    )
    conn.commit()
    conn.close()
