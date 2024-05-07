# enumerate: 열거하다

# fruits = ['apple', 'orange', 'mango']
# for index,item in enumerate(fruits):
#     print(f"{index}. {item}")

coffees = [{'name':'아메리카노','price':2000}, {'name':'라떼','price':3000}]
for index,item in enumerate(coffees):
    # 0. 아메리카노 2000원
    # 1. 라떼 3000원
    print(f"{index}. {item['name']} {item['price']}원")