import sqlite3
from datetime import datetime

def log_metrics(db_path, metrics):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO training_metrics (timestamp, epoch, training_loss, validation_loss, accuracy, perplexity, gpu_usage, cpu_usage, memory_usage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", metrics)
    conn.commit()
    conn.close()
