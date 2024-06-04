#문제: Books라는 테이블 생성
# 각 책의 id, title,author,published_year,in_stock 정보를 저장
# id는 정수, 기본키
# title,author 은 텍스트
# published_year 는 정수형
#in_stock은 불리언 값(0 or 1 저장)

import sqlite3

connection = sqlite3.connect('test1.db')
cursor = connection.cursor()

sql = """
CREATE TABLE Books(
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    published_year INTEGER,
    in_stock BOOLEAN
)
"""

cursor.execute(sql)

connection.commit()
connection.close()