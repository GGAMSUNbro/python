#산술, 비교, 대입, 논리
# 멤버쉽 연산자[in]
coffee = "americano"
print('a' in coffee) # True
print('ameri' in coffee) # True
text ="""""" # 두 문장 이상의 글
news = """ 소매판매 호조로 초반 상승세를 보이던 미국 증시가 중동 정세에 대한 위기감이 고조되면서 급락세로 마감했습니다.
 """
print("증시" in news)

# 슬라이싱 연산자 [:]
car = "tesla"
print(car[0:3]) # tes
print(car[1:3]) # es

# 인덱스 연산자 [[]]
code = "python"
print(code[0]) #p
print(code[3]) #h