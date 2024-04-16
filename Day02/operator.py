#Q
Quiz = input("10,000부터 99,999사이의 양의 정수 n을 입력하시오")
Answer = int(Quiz) // 100
result = int(Answer) % 10
print(f"입력해주신 정수의 100의 자리 숫자는 {result}입니다")