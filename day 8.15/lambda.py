def get_mean(array) : 
    return sum(array) / len(array)
print('mean of [1, 2, 3, 4] = {}'.format(get_mean([1, 2, 3, 4])))
print()

#======================================================================
#1. def 함수 활용
#======================================================================
def print_ops(func, num1, num2) :
    print(func(num1, num2))

def multiply(a, b):
    return a*b
def plus(a, b):
    return a+b

print_ops(multiply, 41, 2)
print_ops(plus, 41, 2)
print()

#======================================================================
#2. lambda 함수 활용
#= =====================================================================
def print_ops(func, num1, num2):
    print(func(num1, num2))

print_ops(lambda a, b : a*b, 41, 2)
print_ops(lambda a, b : a+b, 41, 2)
print()

#======================================================================
#3. 이렇게도 가능
#= =====================================================================
ops = [lambda x, y: x*y, lambda x, y : x/y]
print(ops[0](3,2))
print(ops[1](3,2))
print()

def func1(x, y) : 
    return x*y
def func2(x, y) : 
    return x/y
ops = [func1, func2]
print(ops[0](3,2))
print(ops[1](3,2))
