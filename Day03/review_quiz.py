#Q.1 원화 변환기
# 현재 원화를 입력 하면 달러로 바뀌는 프로그램을 작성하시오

won = int(input("현재 원화를 입력하면 달러로 계산합니다."))
rate = 1393.95
print(f"입력해주신 원화의 달러는 {won/rate} 달러 입니다")

#Q.2 수학연산 프로그램 :

que = int(input("첫 번째 숫자를 입력하세요"))
que1 = int(input("두 번째 숫자를 입력하세요"))
print(f"2 개의 숫자의 합:{que+que1}, 차:{que-que1}, 곱{que*que1}, 몫{que//que1}, 나머지{que%que1}, 제곱{que**que1}을 계산합니다.")


#3.
radius = int(input("원의 반지름:"))
pi = 3.14
print (f"원의 넓이: {radius**2*pi}, 원의 둘레:{radius*2*pi}")
