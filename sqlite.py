import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS employees(
    prenom text,
    nom text
)
""")

d = {"a": "Chris", "b": "Kirk"}
c.execute("INSERT INTO employees VALUES (:a, :b)", d)

conn.commit()
conn.close()