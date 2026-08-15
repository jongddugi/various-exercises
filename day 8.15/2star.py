# **kwargs문법
# *argument는 함수 인자를 받을 때도 쓰고, 함수 밖에서 일반적으로 값을 대입할 때도 사용이 가능함

# **문법은 함수에서만 사용이 가능함.

def function(a, **b) : 
    print('a={}'.format(a))
    print('b={}'.format(b))

function(2, c=3, d =4)
print()

def func(a, *b, c=3, **k) :
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('c={}'.format(c))
    print('k={}'.format(k))

func(1, 2, 3, 4, e=5, f=4, c=2, d=41)
print()
#이름을 안 밝히고 대입해서 받는 argument들은 positional arguemnt라 부르고,(1, 2, 3, 4)
#이름을 명시해서 집어넣는 argument는 keyword argument라 부른다. (e=5, f=4, c=2, d=41)

def function(a, *b, c, d=4, **e) :
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('c={}'.format(c))
    print('d={}'.format(d))
    print('e={}'.format(e))

function(2, 41, 7, 287, c=3, py='thon', ja='va')
print()
