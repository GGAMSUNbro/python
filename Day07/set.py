# set
# list, set (집합)
# 중복 허용 안되는  타입
a = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5,1, 2, 3, 4, 5}
burgerking = {"새우와퍼", "불고기와퍼", "치즈와퍼", "스테이크와퍼"}
momstouch = {"새우와퍼", "치즈와퍼", "싸이버거", "불고기버거"}

# 시프트 원화표시 합쳐
# 합집합 (|)
# union = burgerking|momstouch
#
# # 교집합(&)
# intersection = burgerking & momstouch
#
# # 차집합(-)
# difference = burgerking - momstouch
#
# print(union)
# print(intersection)
# print(difference)
#
# # 추가
# burgerking.add("에그와퍼")
#
# # 삭제
# burgerking.remove("새우와퍼") # 구문법 없는 요소 빼면 에러
# burgerking.discard("새우와퍼") # 신문법 없어도 그냥 지나감
#
# # 전체삭제
# burgerking.clear()
#
# # set() (중요)
# set([1,2,3,1,2,3])
# print(list(result))

news = """We at Tesla believe that we have a moral obligation to continue improving our already best-in-class safety systems. At the same time, we also believe it is morally indefensible not to make these systems available to a wider set of consumers, given the incontrovertible data that shows it is saving lives and preventing injury.

Regulators around the globe have a duty to protect consumers, and the Tesla team looks forward to continuing our work with them towards our common goal of eliminating as many deaths and injuries as possible on our roadways."""

newslist = news.split()
NoDuplicationWords = list(set(newslist))
NoDuplicationWords.sort()
print(NoDuplicationWords)

