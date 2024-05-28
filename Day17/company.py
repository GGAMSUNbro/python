import pandas
from faker import Faker
import random
import math


# 300명
#data = {
#     'name':
#     'age': 20,30,40,50,60
#     'salary': 3000~10000 500 단위,
#     'department': [영업부, 사업부, 개발부, 경영부, 인사부, 생산부],
#     'years_at_company': 1~15,
#     'job_satisfaction': 1~10,
#     'performance_score': 1~100
# }

f = Faker('ko_KR')
Dage = [20,30,40,50,60]
Dsalary = [3000 + x * 500 for x in range(14)]
Ddepartment = ["영업부", "사업부", "개발부", "경영부", "인사부", "생산부"]

data = {
    'name': [f.name() for x in range(300)],
    'age': [random.choice(Dage) for x in range(300)],
    'salary': [random.choice(Dsalary) for x in range(300)],
    'department': [random.choice(Ddepartment) for x in range(300)],
    'years_at_company': [random.randint(1,15) for x in range(300)],
    'job_satisfaction': [random.randint(1,10) for x in range(300)],
    'performance_score': [random.randint(1,100) for x in range(300)],
}

df = pandas.DataFrame(data)
print(df)
df.to_csv('company.csv',index=False,encoding='cp949')