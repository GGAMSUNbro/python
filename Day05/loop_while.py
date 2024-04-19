#loop_while.py
# x = 10
# while x > 0:
#     print("불금인데 학원온거 ㅇㅈ")
#     x -= 1

# while True:
#     x = int(input("숫자 0을 넣어야 멈춤:"))
#     if x == 0:
#         break

#1. 아이스 아메리카노
#2. 아이스 라떼
# while True:
#     x = int(input("숫자 0을 넣으면 멈춤:"))
#     if x == 0:
#         break
#     elif x == 1:
#         print("1. 아이스 라떼")
#     elif x == 2 :
#         print("아이스라떼")



# 유저에게 언어를 고르세요(1.python, 2. java, 3. c++)
#1. python!
#2. java
#3. c++
#4. 프로그램 종료
#그 외는 숫자를 잘못 입력하셨습니다.

# while True:
#     x = int(input("언어를 고르세요(1.python, 2. java, 3. c++)"))
#     if x == 1:
#         print("1. python")
#     elif x == 2:
#         print("2. java")
#     elif x == 3:
#         print("3. c++")
#     elif x == 4:
#         print("4.프로그램 종료")
#         break
#     else:
#         print("잘 못 입력함")

# 계산기 프로그램
# 유저에게 0.프로그램 종료 1. 더하기, 2. 빼기, 3.곱하기, 4.제곱, 5.나누기(몫)
# 그 외 번호는 번호 입력 오류-> 다시 묻기!
# 1번 -> 두 정수를 입력하고 더한 결과값이 나옴
# 2번 -> 두 정수를 입력하고 뺀 결과값이 나옴

while True:
    codenumber = int(input("0.프로그램 종료 1. 더하기, 2. 빼기, 3.곱하기, 4.제곱, 5.나누기(몫)"))
    y = int(input("첫 번째 숫자 입력:"))
    z = int(input("두 번째 숫자 입력:"))
    if  codenumber == 0:
        print("프로그램 종료!")
        break
    elif codenumber == 1:
        print(y+z)
    elif  codenumber == 2:
        print(y-z)
    elif  codenumber == 3:
        print(y*z)
    elif  codenumber == 4:
        print(y**z)
    elif  codenumber == 5:
        print(y//z)
    else:
        print("다시 입력!")