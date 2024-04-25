# length
# len : 문자열 또는 리스트의 길이를 알려주는 기능
# print(len("hello"))
# print(len("python"))
# print(len([2,4,6,8,18]))
#
# # max, min
# print(max([2, 12, 15, 4444, 6666, 11]))
# print(min([2, 12, 15, 4444, 6666, 11]))
#
# # sum
# print(sum([1, 2, 3, 4, 5, 6]))

#Q. 영어 기사 스크랩 해오고, 단어 길이가 6글자 이상인
# 단어들만 출력하기

# news = """Six years after the first Model 3 Performance deliveries, we are launching the new Model 3 Performance:
# a highly differentiated performance trim that leverages Tesla’s latest manufacturing and engineering capabilities
# to create what we consider to be a perfect, high-performance daily driver. """

# word = news.split()
#
# for x in word:
#     if len(x) >= 6:
#         print(x)
#
# fruits = ["apple","banana", "kiwi", "mango", "strawberry", "pineapple","melon"]
# # 문자 길이가 5글자 이하이고, 알파벳 a,e 포함되면 대문자로 출력하고
# # 그게 아니면 그 과일의 문자 길이를 출력하는 프로그램
#
# for x in fruits:
#     if len(x) <= 5 and ("a" in x or "e" in x):
#         print(x.upper())
#     else :
#        print(len(x))

