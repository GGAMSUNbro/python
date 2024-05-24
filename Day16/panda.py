# pandas 라이브러리 설치
import pandas
from faker import Faker

# arr = [1 for x in range(100)]
# s = pandas.Series(arr) # 세로 한 줄을 의미
# print(s)

# data = {
#     'movies':["혹성탈출","범죄도시4","설계자","퓨리오사"],
#     'popcorn':["오리지널 팝콘","어니언 팝콘","캬라멜 팝콘","치즈 팝콘"],
#     'beverage':["콜라","제로콜라","사이다","제로사이다"],
# }
#
# df = pandas.DataFrame(data) # 엑셀 그 자체
# print(df)


#  열 => 학생이름, 학년, 전공, 평균학점 (10명 기준)

# data = {
#     'name':["dexter","stranger","delta","jobs","ilon","lynch","sungmin","dwayne","WS","HG"],
#     'grade':[1,2,2,3,4,5,2,3,4,3],
#     'major':["analyst","magic","nope","apple","comput","stock","logistics","restl","act","sword"],
#     'score':[3.5,4.0,4.5,4.3,4.2,2.5,1.8,4.0,2.0,2.5],
# }
#
# df = pandas.DataFrame(data)
# print(df)
import random
import math

major = ["analyst","magic","nope","apple","comput","stock","logistics","restl","act","sword"]
f = Faker('ko_KR')

data = {
    'name': [f.name() for x in range(1000)],
    'grade': [random.randint(1,5) for x in range(1000)],
    'major': [random.choice(major) for x in range(1000)],
    'score': [round(random.uniform(1,4.5),2) for x in range(1000)],
}
df = pandas.DataFrame(data)

print(df)

df.to_csv('university.csv',index=False,encoding='cp949')
