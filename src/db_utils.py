import sqlite3

def setup_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS training_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        epoch INTEGER,
        training_loss REAL,
        validation_loss REAL,
        accuracy REAL,
        perplexity REAL,
        gpu_usage REAL,
        cpu_usage REAL,
        memory_usage REAL
    )''')
    conn.commit()
    conn.close()
