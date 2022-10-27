"""
    例子1：定义动物，不同的动物实现叫声
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵喵")

def make_noise(animl):
    animl.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)



"""
    例子2：制定空调标准，让不同厂家实现功能
"""

class AC:
    def cool_wind(self):
        # 制冷
        pass
    def hot_wind(self):
        pass
    def swing_wind(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的制冷")
    def hot_wind(self):
        print("美的制热")
    def swing_wind(self):
        print("美的摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力制冷")
    def hot_wind(self):
        print("格力制热")
    def swing_wind(self):
        print("格力摆风")

def make_cool(ac):
    ac.cool_wind()

mind_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(mind_ac)
make_cool(gree_ac)