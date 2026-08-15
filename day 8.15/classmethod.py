# class Example() :
#     def met1(self, value):
#         self.variable = value

#     @classmethod
#     def met2(self, value) :
#         self.variable = value

# a=Example()
# b=Example()

# a.met1(999)

# print(b.variable)

# #a의 variable에 value를 대입시키겠다고 해놓고 b의 variable을 불러와서 print했으므로 에러가 난다.

# class Example() :
#     def met1(self, value):
#         self.variable = value

#     @classmethod
#     def met2(self, value) :
#         self.variable = value

# a=Example()
# b=Example()

# a.met2(999) # a.variable=value가 아닌 Example.variable=value관점에서 변수를 다룰 수 있음
# # 즉, 인스턴스 내부가 아닌 클래스 전체 관점에서의 변수를 다룰 수 있음. 즉 class인스턴스 모두가 공유하는 보편적인 값을 설정하고 싶을 때 사용.

# print(b.variable)

class Member() :
    _ins = []

    def __init__(self, name, height, weight, fat):
        self.name = name
        self.height = height
        self.weight = weight
        self.fat = fat

        self.add_instance(self)

    @classmethod
    def add_instance(cls, ins) :
        cls._ins.append(ins)

a=Member('kim', 180, 77, 24)
a=Member('lhm', 180, 71, 16)
a=Member('Choi', 180, 51, 23)
a=Member('Park', 170, 63, 20)

height_mean = sum([m.height for m in Member._ins])/len(Member._ins)
print(f'height_mean = {height_mean}')

# member_list=[a, b, c, d]
# height_mean = sum([m.height for m in Member_list])/len(member_list)
#이렇게도 쓸 수 있지만 클래스의 캡슐화 측면에서 class변수를 사용하는 것이 좋음