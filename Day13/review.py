# 1. 문자열 뒤집기
# 문자열 my_string 이 매개변수로 주어집니다.
# my_string 을 거꾸로 뒤집은 문자열을 return하도록 함수를 완성하세요

# def reversedWord(my_string):
#     wordList = list(my_string) #[k,o,r,e,a]
#     wordList.reverse() #[a,e,r]
#     reversedWord = "".join(wordList) #aerok
#     return reversedWord


# a = reversedWord("hello world")
# print(a)
#
# # 2. 미완성된 할일 찾기
# # todo_list에 있는 할 일 중,
# # finished 배열을 통해 아직 끝내지 못한 일들을
# # 순서대로 배열에 담아 반환하는 함수 만드세요
#
# todolist = ["prblemsolving", "praciceguitar", "swin", "studytgragh"]
# donelist = [True, False, True, False]
#
# def filterDoneList(todolist, donelist):
#     return [item for index, item in enumerate(todolist) if donelist[index] ==True]

# class Animal:
#     def __init__(self,name,bread):
#         self.name = name
#         self.bread = bread
#     def eat(self):
#         print("냠냠냠")
#
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print("멍멍")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("냐옹")
#
# a = Dog("킹","이탈리안")
#
# a.eat()
#
#
# class Animal:
#     def __init__(self, name, typ):
#         self.name = name
#         self.typ = typ
#
#     def eat(self):
#         print("냠냠냠")
#
#     def sound(self):
#         pass
#
#     def introduce(self):
#         print(f"이름:{self.name}, 종:{self.typ}")
#
# b = Animal("킹","이탈리안")
# b.eat()
# b.introduce()



# 퀴즈
# 관리자, 편집자, 뷰어 라는 각각 사용자가 존재합니다.
# 모두 접근하기라는 함수를 가지고 있습니다.
# 모두 username이라는 속성도 가지고 있습니다.

# 관리자 - 유저만들기
# 편집자 - 편집하기
# 뷰어 - 조회하기



class system:
    def __init__(self, username):
        self.username = username

    def access(self):
        pass

class maintenence(system):
    def maker(self):

    def access(self):
        print("접근 가능합니다 객체가")



class editor(system):
    def edit(self):

    def access(self):
        print("접근 가능합니다 객체가")


class viewer(system):
    def search(self):





















