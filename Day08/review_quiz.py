#정수 n에 따른 수열 합산 퀴즈
# 양의 정수 n을 입력으로 받아들여 n의 홀짝성에 따라 다른 계산을 수행하는 프로그램
#만약 n이 홀수라면 n이하의 모든 홀수의 합을 반환
# 만약 n이 짝수라면 n이하의 모든 짝수의 제곱의 합을 반환
#예시 n =5
# 결과 = 9

# n = int(input(" 양의 정수 입력:"))
# result = 0
# if n % 2 == 1:
#     for x in range(n+1):
#         if x % 2 == 1:
#             result += x
# else:
#     for x in range(n + 1):
#         if x % 2 == 0:
#             result += x ** 2
# print(result)

# 배열 변환 기반 조건적 연산 퀴즈
# 정수 배열 arr 와 자연수 k 가 주어집니다. 이때 k의 홀짝성에 따라 배열에 다른 연산 적용
# 만약 k가 홀수라면 배열arr의 모든 원소에 k를 곱하고, k가 짝수라면 모든 원소에 k를 더함

# arr = [1,2,3]
# k = int(input("자연수 입력:"))
# newList = []
# if k % 2 == 1:
#     for x in arr:
#         newList.append(x * k)
# else:
#     for x in arr:
#         newList.append(x + k)
# print(newList)