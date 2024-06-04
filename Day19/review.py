#1. 핸드폰 번호 가리기
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 떄
# 고객의 전번 일부를 가림. 전화번호 문자열 phone_number로 주어졌을 때, 전화번호
# 맨 뒤 4 자리만 표시, 나머지는 *로 가린 함수



def solution(number):
    answer = ""
    for index,item in enumerate(list("number")):
        if len(number) - index <= 4:
            answer += item
        else:
            answer += "*"
    return answer

# 내 버전
# def soluton(phone_number):
#     for x in phone_number:
#         if len(phone_number)>=4:
#             phone_number += "*"
#         else:
#             phone_number += x
#         return phone_number
#
# print(solution("number"))



# 2. 영어가 싫어요
# 영어가 싫은 강사님은 영어로 표기된 숫자를 수로 바꾸려한다.
# 문자열 numbers가 매개 변수로 주어질 때, numbers로 return하는 함수



def solution1(numberStr):
    numberdict = { "zero" : 0,
          "one" : 1,
          "two" : 2,
          "three" : 3,
          "four" : 4,
          "five" : 5,
          "six" : 6,
          "seven" : 7,
          "eight" : 8,
          "nine" : 9,}
    for x in list(numberdict.keys()):
        if x in numberStr:
            numberStr = numberStr.replace(x,str(numberdict[x]))
    return(numberStr)

# # 만약 onetwothree라면 123이 나와야됨
#
# roomnumber = "onetwothree"
# for x in roomnumber:
#     if x in
#
#
#
# for x in roomnumber:
#     roomnumber += x