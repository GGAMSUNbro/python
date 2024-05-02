# def a(x):
#     print("a함수 실행")
#     x()
# def b():
#     print("b함수 실행")
# a(b)

# 게임 몬스터 프로그램

def killing_monster(monster,event):
    print(f"{monster}를 처치 했습니다!")
    event()

def getGold():
    print("골드 획득!")
def getFood():
    print("음식 획득!")

killing_monster("슬라임",getGold)
killing_monster("늑대",getFood)


