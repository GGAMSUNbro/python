#Q. 문자열 섞기
# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서
#저장한 배열은 return하는 solution 함수


def solution(my_str,n):
    arr = []
    word = ""
    for index, item in enumerate("adsf",1):
        word += item
        if index % 6 == 0:
            arr.append(word)
            word = ""
    arr.append(word)
    return arr
print(arr)

# 내버전
# st = "abvsd323kj"
#
# def solution(my_str,n):
#     newStr = my_str.split()
#     [newStr.append(x) if len(newStr) <= n else newStr.append(",") for x in newStr]
#     return newStr


# Q. JadenCase 문자열 만들기
# 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
#단, 첫 문자가 알파벳이 아닐 떄에는 이어지는 알파벳은 소문자
# 문자열 s가 주어졌을 때 리턴하는 함수

def solution1(s):
    return "".join([x.capitalize()+" " for x in s.split(" ")])

# if str2[0] == str:
#     str2[0].upper()
# else:
#     print("str2")