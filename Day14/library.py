import math
import random

# 랜덤으로 여섯 개의 숫자를 뽑아주는 프로그램 [1~45] 중복 x
# print(random.randint(0,10000))

# lotto = []
#
#
# while True:
#     num = random.randint(0, 45)
#     if lotto.count(num) == 0 :
#         lotto.append(num)
#         if len(lotto) == 6:
#             break
#
# lotto.sort()
# print(lotto)

# print(random.choice(["사과","바나나","집에가고싶다"]))


#유저에게 6개 입력 받고 몇 개맞았는지, 몇 등인지 알려주기


lotto = []
while True:
    num = random.randint(0, 45)
    if lotto.count(num) == 0 :
        lotto.append(num)
        if len(lotto) == 6:
            break

yourNumber = []
for x in range(6):
    yourNumber.append(int(input(f"{x}. 번호 입력")))
rank = 6
for x in lotto:
    if yourNumber.count(x) > 0:
        rank -= 1
print(f"로또: {lotto}")
print(f"당신: {yourNumber}")
print(f"{rank}등 축하드립니다!")