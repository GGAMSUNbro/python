class Bird:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def lay(self):
        print(f"{self.name}가 알을 낳다")

class Flyalbe:
    def fly(self):
        print("날아 다니다.")

class Eagle(Bird, Flyalbe):
    def crawl(self):
        print(f"{self.name}이 사냥합니다.")

class Penguin(Bird):
    def swim(self):
        print(f"{slef.name}이 수영합니다.")
