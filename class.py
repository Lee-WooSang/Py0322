
class Person:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name

    def introduce2(self, message):
        print(message)

p1 = Person("이우상",50)

hname = p1.get_name()

print(hname)

p1.introduce2("테스트")


