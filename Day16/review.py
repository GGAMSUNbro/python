# Q1. 조건에 맞게 수열 변환하기
# 정수 배열 arr 와 자연수  k가 주어집니다. 만약 k가 홀수라면
# arr의 모든 원소에 k를 곱하고, k가 짝수라면 arr의 모든 원소에 k 더함
# 이를 return하는 함수 작성

# def solution(arr, k):
#     return [x * k if k % 2 == 1 else x + k for x in arr]

#내 버전 아래
# arr = [1,2,3,4]
# k = int(k)
#     if k % 2 == 1:
#         arr.append(*k)
#     else:
#         arr.append(+k)
#     return arr
#
# arr1 = [1,2,3,4,5]
#
# a = solution(arr1,2)
# print(a)



# Q2. A강조 하기
# 문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면
# 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환

# def solution(myString):
# "".join()[ 'a' if x == 'A' else x.lower() for x in "myString"]

# 내 버전 아래
# def solution1(myString):
#     newmyString = ""
#     for x in myString:
#         if x == "a":
#             newmyString += newmyString.upper(str(myString))
#         else:
#             newmyString += newmyString.lower(str(myString))
#         return newmyString()
#
# print(solution1("aBBBAaa"))

# Q3. 오늘 날짜 [05-24, 05-25.... 한 달 뒤까지] 담긴 문자열 출력

import datetime

def solutrion3(x):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=x)
    return next_week.strftime("%m-%d")

a = [solutrion3(x) for x in range(31)]
print(a)