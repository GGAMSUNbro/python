import matplotlib.pyplot as plt
import pandas
from faker import Faker
import random
import math


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
# print(df)
df.to_csv('company.csv',index=False,encoding='cp949')
#
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 35]

# plt.plot(x,y)
# plt.show()

x = df['age']
y = df['salary']

plt.hist2d(x,y)
plt.show()