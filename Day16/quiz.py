# 메가커피 당일 구매 데이터 1000명

# 이름 메뉴 몇시 결제수단 매장/포장
import pandas
from faker import Faker
import random
import math
import datetime

# 가중치 넣기
nameF = Faker('ko_KR')
menu = ["아메리카노","카페라떼","아이스초코","초코쿠키","과일주스"]
using = ["카드","현금","비트코인"]
howEat = ["매장","포장"]

# def get_random_time():
#     s = datetime.datetime.strftime("07:00","%H:%M")
#     e = datetime.datetime.strftime("22:00","%H:%M")
#     total = int((e-s).total_seconds() / 60) # 전체 몇분
#     random_minutes = random.randint(0,total)
#     return s + datetime.timedelta(minutes=random_minutes)
# print(get_random_time().strf)

megaData = {
    'name':[nameF.name() for x in range(1000)],
    'menu':[random.choice(menu) for x in range(1000)],
    'time':[random.randint(8,24) for x in range(1000)],
    'using':[random.choice(using) for x in range(1000)],
    'howEat':[random.choice(howEat) for x in range(1000)],
}

mgdata = pandas.DataFrame(megaData)

print(mgdata)

mgdata.to_csv('megadatAAA.csv', index=False, encoding='cp949')
