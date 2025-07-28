class Human():
    def __init__(self, life, age, hair, money):
        self.life = life
        self.age = age
        self.hair = hair
        self.money = money
    def howOld(self):
        print(f"is {self.age} years old")

a = Human(True, 25, "Blonde", 12345678)
a.name = "Max"
a.pi = 3.14159


