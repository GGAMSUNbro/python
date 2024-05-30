import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('bicycle.csv',encoding='cp949')

def change(x):
    return x.split("_")[0]

df['시작_대여소명'] = df['시작_대여소명'].apply(change)
data = df['시작_대여소명'].value_counts()
plt.rcParams['font.family'] = 'Malgun Gothic'
data.plot.pie()
plt.show()