# Q. 문자열 잘라서 정렬하기
# 문자열 myString가 주어집니다. "x"를 기준으로 해당 문자열을 잘라내
# 배열을 만든 후 사전순으로 정렬한 배열 return. solution
def solution(myString):
    filterdList = list(filter(lambda x: len(x) !="","axxfxxfx".split("x")))
    filterdList.sort()
    return filterdList


#Q 배열 원소 삭제하기
# 정수 배열 arr과 delete_list가 있습니다.
# arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은
# 기존의 arr에 있던 순서를 유지한 배열을 return. solution


arr = [233, 1111, 333, 555]
delete_list = [94, 333, 1111 ]


def solution1(arr,delete_list)
    return list(filter(lambda x: x not in delete_list.arr))

# 내 버전
# def solution1(arr,delete_list):
#    c = [ "" if x in delete_list else x for x in arr ]
#    return print(c)

# Q. 최댓값 만들기
# 정수 배열 numbers가 매개변수로 주어집니다.
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값 return solution

def solution2(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        return numbers[0] * numbers[1]
    else:
        return numbers[-1] * numbers[-2]



#  내 버전
numbers = [1,2,3,4,5,]

def solution2(numbers):
   d =[ numbers.append(*x) for x in numbers ]
   return print(max(d))