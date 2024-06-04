import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

sql = """
INSERT INTO COFFEE (id, coffeeName, coffeePrice, coffeeKcal)
VALUES (1,'americano',2500,10);
"""

cursor.execute(sql)

connection.commit()
connection.close()