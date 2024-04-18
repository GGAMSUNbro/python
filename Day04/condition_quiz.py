#1. 정수를 입력받고
#양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수
#판별해주는 프로그램
# ex) -5 => 음의 홀수, 0 => 0, 3 => 양의 홀수

# score = int(input("점수 입력:"))
# if score > 0:
#     if score % 2 == 0:
#         print("양의 짝수")
#     else:
#         print("양의 홀수")
# elif score == 0 :
#     print("0")
# else:
#     if score % 2 == 0:
#         print("음의 짝수")
#     else:
#         print("음의 홀수")
#
# num = int(input("정수 입력"))
# isPositive = num > 0
# isNegative = num < 0
# isOdd = num % 2 == 1
# isEven = num % 2 == 0
# if isPositive and isOdd:
#     print("양의 홀수")
# elif isPositive and isEven:
#     print("양의 짝수")
# elif isNegative and isOdd:
#     print("음의 홀수")
# elif isNegative and isEven:
#     print("음의 짝수")
# else:
#     print("0")

# datax = int(input("x축 좌표값 입력"))
# datay = int(input("y축 좌표값 입력"))
# side1 = datax >0 and datay > 0
# side2 = datax < 0 and datay > 0
# side3 = datax <0 and datay < 0
# side4 = datax > 0 and datay < 0
# if side1 :
#     print ("1사 분면")
# elif side2:
#     print("2사 분면")
# elif side3 :
#     print("3사 분면")
# elif side4 :
#     print("4사 분면")
# else:
#     print("0")

fee = int(input("구매 금액을 입력하세요!"))
discount1 = 0.2
discount2 = 0.1
discount3 = 0.05
discount4 = 0
if fee >= 200000:
    print(f"구매 금액은 {fee}, 할인율은 {discount1}, 할인금액은 {fee*discount1}, 최종 결제 금액은 {fee-(fee*discount1)}")
elif fee >= 100000:
    print(f"구매 금액은 {fee}, 할인율은 {discount2}, 할인금액은 {fee*discount2}, 최종 결제 금액은 {fee-(fee*discount2)}")
elif fee >= 50000:
    print(f"구매 금액은 {fee}, 할인율은 {discount3}, 할인금액은 {fee*discount3}, 최종 결제 금액은 {fee-(fee*discount3)}")
else:
    print(f"구매 금액은 {fee}, 할인율은 {discount4}, 할인금액은 {fee * discount4}, 최종 결제 금액은 {fee - (fee * discount4)}")