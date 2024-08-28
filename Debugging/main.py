class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def increaseage(self):
        self.age += 1

    def decreaseage(self):
        self.age -= 1

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

atil = person("Atil", 5)
atil.decreaseage()
atil.decreaseage()
atil.decreaseage()
atil.decreaseage()
atil.decreaseage()
atil.decreaseage()
atil.decreaseage()

print(atil)









class Myclass:

    def __init__(self):
        print("initialized")

    def print1(self):
        print("python")

Myclass = Myclass()
Myclass.print1()
