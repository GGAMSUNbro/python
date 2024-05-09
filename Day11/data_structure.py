# 기본 자료 구조: 데이터를 어떻게 보관하고 다루는지에 대한 방법들
# list: 순서 있고, 중복 가능
# set : 순서 없고, 중복 불가능
# dict : k[중복 안됨]-v[중복 가능] 형태로 저장
# tuple:(사과,바나나,키위) 수정 불가능

# 심화 자료 구조:
# graph : 그래프 자료구조 [지도,미니맵,경로 최적화]
# tree : 트리 자료구조 [단어 검색]


# names = ['아메리카노','라떼','바닐라']
# prices = [2000, 2500, 3000]
# menu = []
# for index, item in enumerate(names):
#     menu.append({'name': item, 'price': prices[index]})
#
# print(menu)

# names = ['아메리카노','라떼','바닐라']
# prices = [2000, 2500, 3000]
# x = dict(zip(names,prices))
# print(x)

# 과일 이름 리스트:
# 과일 가격 리스트:
# zip으로 묶어서 k-v 형태 나타내기

fruits = ['mango','coconut','musket']
prices = [4000, 5000, 7000]

for (x,y) in zip(fruits,prices):
    print(f"{x},{y}")

for index, (x,y) in enumerate(zip(fruits,prices)):
    print(f"{index}. {x},{y}")

menu = [{'name': x, 'price': y} for (x,y) in zip(fruits,prices)]
print(menu)

# text = "apple banana apple strawberry banana"
#[{"단어":"apple","글자수":5},{"단어":"banana","글자수":6}...]
text = "apple banana apple strawberry banana"
a = [{"단어": x, "글자수": len(x)} for x in text.split(" ")]


















