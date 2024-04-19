# Q.3개의 정수 평균
# num1 = int(input("첫 번째 정수를 입력하세요."))
# num2 = int(input("두 번째 정수를 입력하세요."))
# num3 = int(input("세 번째 정수를 입력하세요."))
# avg = (num1 + num2 + num3)/3
# print(f"입력하신 3개의 정수 평균은 {avg}입니다!")

#Q.2 가장 큰 정수 찾기 프로그램
# num1 = int(input("첫 번째 정수를 입력하세요."))
# num2 = int(input("두 번째 정수를 입력하세요."))
# num3 = int(input("세 번째 정수를 입력하세요."))
# if num1 > num2 and num1 > num3:
#     print(f"입력하신 숫자 중 가장 큰 수는 {num1}입니다.")
# elif num2 > num1 and num2 > num3:
#     print(f"입력하신 숫자 중 가장 큰 수는 {num2}입니다.")
# else :
#     print(f"입력하신 숫자 중 가장 큰 수는 {num3}입니다.")

#Q.3 입력한 정수의 배수 출력 프로그램
num = int(input("정수를 입력해주세요!"))
for x in range(101):
    if x % num == 0:
        print(x)