class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def age(self):
        return self._age

p=Person('Ihm',29)
p.age() # argument를 받아야함
print(p.age())
print()
#=======================================================
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property # 추가됨
    def age(self):
        return self._age

p=Person('Ihm',29)
p.age # property가 붙은 함수는 argument를 받지 못함
print(p.age)
print()
 #=======================================================
 #예시1
 #=======================================================

class Member() :
    def __init__(self, height, weight, fat):
        self.height = height
        self.weight = weight
        self.fat = fat

    @property
    def bmi(self) : 
        height_in_meter = self.height/100
        return self.weight/height_in_meter**2

i = Member(176, 71, 13)
print('bmi = {}'.format(i.bmi))# i.bmi()로 괄호를 붙이면 class내부적으로 어떤 기능을 할 것처럼 보임.
#값만 얻고 싶은 경우면 @property 사용
print()

 #=======================================================
 #예시2
 #=======================================================

class Member() :
    def __init__(self, height, weight, fat):
        self.height = height
        self.weight = weight
        self.fat = fat

    @property
    def height(self) : 
        return self._height

    @height.setter
    def height(self, h) :
        self._height = h

i = Member(176, 71, 13)
print('height = {}'.format(i.height))
i.height = 166
print('height = {}'.format(i.height))
print()
 #=======================================================
 #예시3
 #=======================================================

class Member() :
    def __init__(self, height, weight, fat):
        self.height = height
        self.weight = weight
        self.fat = fat

    @property
    def height(self) : 
        return self._height

    @height.setter
    def height(self, h) :
        if h < 0: print('[Warning] negative height?')
        self._height = h

i = Member(176, 71, 13)
print('height = {}'.format(i.height))
i.height = -166
print('height = {}'.format(i.height))
print()
 #=======================================================
 # 악용 예시1
 #=======================================================

class Member() :
    def __init__(self, height, weight, fat=14.0):
        self.height = height
        self.weight = weight
        self.fat = fat

    @property
    def height(self) : 
        return self._height

    @property
    def weight(self) : 
        return self._weight

    @height.setter
    def height(self, value) :
        setattr(self,'_weight', value)

    @weight.setter
    def weight(self, value) : 
        setattr(self, '_height', value)

a = Member(170, 71)
a.height = 190
print('height of a ={}'.format(a.height))