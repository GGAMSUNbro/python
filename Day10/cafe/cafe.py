#Q
# ex: 1. 커피판매 -> 1. 아메리카노 2000원, 2. 라떼 2500원 , 3. 바닐라라떼 3000원
# 2. 커피 메뉴 추가 > 커피 이름 :
#                 > 커피 가격:
# 3. 프로그램 종료




coffeeList = [{'name': '아메리카노', 'price': 2000}, {'name': '라떼', 'price': 2500}, {'name': '바닐라라떼', 'price': 3000}]

while True:
    option = int(input( "1. 커피 판매 2. 커피 메뉴 추가 3. 프로그램 종료"))
    if option == 1:
        for index,item in enumerate(coffeeList):
            print(f"{index}. {item['name']} {item['price']}원")
        option = int(input("커피입력:"))
    elif option == 2:
        newCoffeeName = input("커피 이름:")
        newCoffeePrice = int(input("커피 가격:"))
        newCoffeeMenu = {'name':newCoffeeName,'price':newCoffeePrice}
        coffeeList.append(newCoffeeMenu)
    elif option ==3:
        print("프로그램 종료")
        break
    else:
        print("없는 선택지:")


