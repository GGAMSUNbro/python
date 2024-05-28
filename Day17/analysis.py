import pandas

df = pandas.read_csv("company.csv",encoding='cp949')
# 기본 열 뽑기
# print(df['name']) # 한 열
# print(df[['name','salary','age']]) # 다중 열

# 조건으로 열 뽑기
# print(df[df['salary'] >= 7000])
# print(df[df['years_at_company'] >= 7])
# a = df['salary'] >= 5000
# b = df['years_at_company'] >= 7
#
# print(df[a & b])

# 근속연도 10, 만족도 8, 수행도 80인 사람 뽑기
# c = df['years_at_company'] >= 10
# d = df['job_satisfaction'] >= 8
# e = df['performance_score'] >= 80
#
# print(df[c&d&e])

# 열 추가
# df['test'] = df['age'] * df['years_at_company']
# 5년 이하 - 사원
# 10년 이하 - 과장
# 15년 이하 - 부장
def makeRank(x):
    if x <= 5:
        return "사원"
    elif x <= 10:
        return "과장"
    else:
        return "부장"
# apply 함수
# df['rank'] = df['years_at_company'].apply(makeRank)
# print(df)

# performance_score
# 20점 - 권고사직
# 50점 - 직급 유지
# 80점 - 보너스
# 100점 - 승진

def valueate(x):
    if x <= 20:
        return "권고사직"
    elif x <= 50:
        return "직급 유지"
    elif x <= 80:
        return "보너스"
    else:
        return "승진"

df['value'] = df['performance_score'].apply(valueate)
print(df)
print(df.info)
print(df.describe())
print(df.sort_values(by='age'))
