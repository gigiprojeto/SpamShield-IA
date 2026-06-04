import sqlite3

conn = sqlite3.connect("database/spamshield.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensagem TEXT,
    resultado TEXT
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")
