#Q1. 제일 작은 수 제거하기
# 정수를 저장한 배열, arr에서 가장 작은 수를 제거한 배열 리턴하는 함수
# solution을 완성해주세요
# 단, 리턴하려는 배열이 빈 배열인 경우 배열에 -1을 채워 리턴.
# EX: arr = [4,3,2,1] 이면 [4,3,2] 를 리턴하고 , [10]이면 [-1] 리턴
#
# def solution(arr):
#     if len(arr) == 1:
#         return [-1]
#     else:
#         arr.remove(min(arr))
#         return arr


# Q2. 문자열 섞기
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아 가면서 한 번씩 등장하는 문자열 리턴하는 솔루션 함수

# def solution1(str1,str2):
#     text = ""
#     for x in range(len(str1)):
#         text += str1[x]
#         text += str2[x]
#     return text
#
# print(solution1("aaa","bbb"))

# Q3. x 사이의 개수
# 문자열 myString가 주어짐. myString을 문자 "x"를 기준으로 나눴을 때
# 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을 return 하는 solution 함수 구하기

def solution3(str):
    return list(map(lambda x : len(x), filter(lambda x: len(x) > 0, "oxxoxxoo".split("x"))))



# Q4. 5명씩
# 문제 : 최대 5명씩 탑승가능한 놀이기구에 줄서고 있는 사람들
# 사람 이름이 담기 문자열 리스트 names가 주어질 때, 앞에서 부터 5명씩 묶은 그룹의
# 가장 앞에 있는 사람 이름을 담은 리스트 리턴
# 마지막 그룹이 5명 되지않아도 포함


arr = ["jason", "Irepublic", "Talor","Tony", "ilon","Jackson"]

def solution4(arr):
    return [item for index,item in enumerate(arr) if index % 5 == 0]

print(solution4(arr))

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "소리 내는중"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()},,,멍멍"

a = Dog("흰둥","하얀개")
print(a.speak())