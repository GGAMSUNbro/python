import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

sql = """
CREATE TABLE COFFEE(
    id INTEGER PRIMARY KEY,
    coffeeName TEXT,
    coffeePrice INTEGER,
    coffeeKcal INTEGER
)
"""

cursor.execute(sql)

connection.commit()
connection.close()