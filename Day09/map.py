# # map(how, target) : target을 바꿔주기
# numList = [i for i in range(101)]
# # [100, 101, 102, 103..]
# result = list(map(lambda x: x+100, numList))
# print(result)
#
# #filter: target을 필터링해줌
# result1 = list(filter(lambda x: x% 2 == 0, numList))
# print(result1)
# # 5글자 이하 살리기
# fruits = ["apple","banana","cherry","kiwi"]
# result2 = list(filter(lambda x : len(x) <= 5,fruits))
# print(result2)
# # 알파벳 a가 포함되어있는거 살리기
# result3 = list(filter(lambda x : 'a' in x ,fruits))
# print(result3)
emailList = ["abc@naver.com","mega@gmail.com","koreait@daum.net"]
# map -> 유저아이디로 바꾸기

print(list(map(lambda x: x.split("@")[0],emailList)))
