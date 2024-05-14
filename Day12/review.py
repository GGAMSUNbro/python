# class Dog:
#     # 생성해주는 친구(=생성자)
#     def __init__(self,a,b):
#         self.name = a
#         self.breed = b
#
#     def barking(self):
#         print("멍멍!")
#
# a = Dog("월트","달마시안")
# a.barking()



# Book 클래스 만들기
# 제목, 작가를 가지는 클래스

class Book:
    def __init__(self,title,writer):
        self.title = title
        self.writer = writer

    def display_info(self):
        return f"책 제목:{self.title} 작가 : {self.writer}"

#     display_info -> return str 문자열로 책 제목:{} 작가: {}

a = Book("이기는 투자","피터 린치")
print(a.display_info())

print(a)