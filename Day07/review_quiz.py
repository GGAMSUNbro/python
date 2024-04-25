#Q1. 문자열 문자 반복 프로그램
# 주어진 문자열 word 의 각 문자를 정수 n 만큼 반복하여 새로운 문자열 생성하는 프로그램
#ex : 입력 word = "abc", n = 3
# 결과 : "aaabbbccc"
# word = input("문자를 입력:")
# times = int(input("몇 번 반복?:"))
#
# newWord = ""
# for x in word:
#     newWord += x * times
# print(newWord)

#Q2.  모음 대문자화 프로그램
#사용자로부터 문자열을 입력받아 그 문자열 내의 모든 모음(a,e,i,o,u)만 대문자로 변환하는 프로그램 작성

# word = input("문자를 입력:")
#
# newWord = ""
# for x in word:
#     if x in "aeiou":
#         newWord += x.upper()
#     else:
#         newWord += x
# print(newWord)

#Q3. 소문자는 대문자화, 대문자는 소문자화

# word = input("문자 입력:")
#
# newWord = ""
# for x in word:
#     if x.isupper():
#         newWord += x.lower()
#     else:
#         newWord += x.upper()
# print(newWord)

#Q4. 단어를 입력했을 때
# 자음은 대문자화 해서 출력하기
# ex) hello > HeLLo

word = input("단어 입력:")

newWord = ""
for x in word:
    if x not in "aieou":
        newWord += x.upper()
    else:
        newWord += x
print(newWord)
