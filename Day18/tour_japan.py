import pandas
import matplotlib.pyplot

df = pandas.read_csv('japan.csv')
# 2023년에 각 나라별로 방문자 수를 알고 싶음
year_2023 = df[(df['Year'] == 2023)] & (df['Purpose_of_visit_to_Japan'] == 'Tourism')
a = year_2023.groupby('Country/Area')['Visitor Arrivals'].sum()
print(a)