#comprehension
# [0~100] 리스트 출력

# word = []
# for x in range(101):
#     word.append(x)
# print(word)

# a = [x for x in range(101)]
# print(a)
# # "apple" => [a,p,p,l,e]

# word = []
# for x in "apple":
#     word.append(x)
# print(word)
# b = [ x for x in "apple"]
# # C는 0~10까지
# c = [x for x in range(11) if x % 2 == 0]
# # 0~100 홀수만 리스트
# d = [x for x in range(101) if x % 2 ==1]
# 0~100 짝수를 제곱인 형태인 리스트
# [0,4,16...]
# e = [x**2 for x in range(101) if x % 2 == 0]
# print(e)
# 0~10 홀수에서 10을 더한 리스트
# [11,13,15,17,19]
# f = [ x+10 for x in range(11) if x % 2 == 1 ]
# print(f)

# => 문자 길이대로 바꾸기
fruits = ["apple","banana","kiwi","grape","orange"]
# g = [len(x) for x in fruits if "i" in x]
# print(g)

# 매핑 컴프리헨션
# 홀수는 10 짝수 20 +
# h = [x + 10 if x % 2 == 1 else x + 20 for x in range(101) ]


fruits = ["apple","banana","kiwi","grape","orange"]
# 5글자 이하이면 글자의 길이로 나타내고, 아니면 대문자화 하기
# [ 5, BANANA]
i = [len(x) if len(x) <= 5 else x.upper() for x in fruits]
print(i)
