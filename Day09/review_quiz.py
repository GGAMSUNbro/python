#Q  이메일 주소 분리 퀴즈
# "사용자로부터 전체 이메일 주소를 입력받습니다.
# username@example.com 과 같은 형식
#예시 입력 : "itKorea@naver.com"
# 출력 : {user : "itKorea", domain: "naver.com"}

# def splitEmail(email):
#     arr = email.split("@")
#     return {"user": arr[0], "domain":arr[1]}

#Q 문자열 변환 마법 퀴즈
# 사용자로부터 문자열 입력 받고, 입력된 문자열은 두 가지 마법적 변환 거침
# 1. 문자열을 뒤집어 순서 바꿈
# 2. 문자열의 문자들을 알파벳 순서로 정렬
#ex: input : mega
# output : {reversed:"agem", sorted:"aemg"}

# def spellingMagic(word):
#     spellingList = list(word) # [m, e, g, a]
#     spellingList.sort() # [a,e,g,m]
#     result = "". join(spellingList) # list -> str
#
#     spellingList1 = list(word)
#     spellingList1.reverse()
#     result1 ="". join(spellingList1)
#     return{"sorted":result, "reversed":result1}
#
# print(spellingMagic("koreaIt"))

# 정수 n이 주어졌을 때, 홀수면 "odd" 짝수면 "even"을 돌려주는
# 함수 만들기

def basic(x):
    if x % 2 == 1:
        return "odd"
    else:
        return "even"

num = int(input("정수"))
print(basic(num))