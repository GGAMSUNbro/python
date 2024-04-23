# Q1. 음료 선택 및 잔돈 계산 프로그램 3 4 35
drink = int(input("1. 아메리카노 2.레몬에이드 3.카페라떼"))
fee = int(input("지불하신 비용은?"))
if drink == 1:
    print(f"아메리카노이며 잔돈은 {fee-3000}")
elif drink == 2:
    print(f"레몬에이드며 잔돈은 {fee-4000}")
elif drink == 3:
    print(f"카페라뗴 잔돈은 {fee-3500}")
else :
    print("선택하신 번호의 음료는 XX")

#Q2.
bus = int(input("노선의 종류 입력: 1. 시내버스1200 2. 광역버스2000 3. 마을버스1000"))
fee = int(input("지불하신 비용은?"))
age = int(input("할인율 적용을 위해 나이 입력:"))

if age <= 7 or age >= 65:
    print("위 고객은 무료")
elif 8<= age and age <= 19 :
    if bus == 1:
        print(f"시내버스 요금은 {1200*0.7}원 입니다.(청소년 할인적용)")
    elif bus == 2:
        print(f"시내버스 요금은 {2000 * 0.7}원 입니다.(청소년 할인적용)")
    elif bus == 3:
        print(f"시내버스 요금은 {2000 * 0.7}원 입니다.(청소년 할인적용)")
    else:
        print("해당 버스 번호는 없음")

#Q3. 짝수 배수 출력 프로그램
num = int(input("정수를 입력하시오"))
for x in range(2,101) :
    if x % num == 0 and x % 2 == 0:
        print(x)
