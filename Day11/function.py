# function : 명령어 묶음
# 내장 함수: print, input, len, sum, int,zip,enumerate....
# def name(args):
#    로직
#    retunr value

#디폴트 매개변수
# def hello(x="icecream"):
#     return f"{x} hello"

# lambda 함수
# lambda x : x+1

#콜백함수
# 매개변수에 함수를 넣는 것

#map, filter
#map(how,what): what 을 how로 바꾸기
print(list(map(lambda x: x + 5 , [1,2,3,4,5])))

# filter(how,what): what을 how로 걸르기
print(list(filter(lambda x: x% 2 == 0, [1,2,3,4,5])))