def plane(a, b, c, d):
    print("{}x+{}y+{}z = {}".format(a, b, c, d))

plane(*[3, 4.1, -7, 2.3])
print()
#list에 있는걸 (풀어서) argument로 보내는 뜻
# 값을 '집어넣는'쪽의 list나 tuple의 [], ()을 없애는 역할을 합니다.
# 이걸 starred expression이라고 부름

a, *b = 3, 4, 5
print(a)
print(b)
print()

#starred assignment 값을 대입하고 남는걸 star에 넣는것
a, b, *c = 3, 4
print(a)
print(b)
print(c)

# 함수에서 *을 쓸 때는 앞에 필수적인 argument를 개수만큼 받고
#만약에 추가 argument를 무제한으로 받고 싶을 때 이 문법을 사용하면 됨.
def func(a, b, c, *d) :
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('c={}'.format(c))
    print('d={}'.format(d))

func(1, 2, 3, 4, 5, 6)

#star argument를 쓰는 가장 대표적인 함수 : print
