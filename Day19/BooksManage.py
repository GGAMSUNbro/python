import sqlite3

connection = sqlite3.connect('test1.db')
cursor = connection.cursor()

sql = """
INSERT INTO Books (id, title, author, published_year, in_stock)
VALUES (3,'winning','lynch',2022,True);
"""

cursor.execute(sql)

connection.commit()
connection.close()