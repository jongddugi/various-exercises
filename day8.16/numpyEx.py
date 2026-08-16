import numpy as np

a= np.array([[0, 1, 2], [3, 4, 5]])
print("a[0] = {}".format(a[0]))
print("a[:,0]={}".format(a[:,0]))
print()
# 행렬 여러 수의 데이터 다룰 땐 list보다 numpy

import numpy as np
a = np.array([[2, 4, 6],[10, 12, 14]])
print("mean of a = {}".format(np.mean(a)))
print("std of a = {:.3f}".format(np.std(a)))
print()

#=======================================================
#ex1)
#=======================================================

import numpy as np

x = np.array([[2, 4, 6], [10, 12, 14]])
print(x.mean())
print(x.std())
print(np.mean(x))#위와 기능은 같으나 np를 활용하면 list나 tuple에도 적용할 수 있음.
print(np.std(x))
print()

#=======================================================
#ex2)
#=======================================================

import numpy as np

kim = [4.0, 6.0, 8.0]
park = [0.0, 7.0, 12.5]
ihm = [5.0, 6.0, 10.0]
jeong = [3.5, 6.0, 10.0]
choi = [4.0, 7.0, 13.0]
meal = np.array([kim, park, ihm, jeong, choi])
print(meal.shape)

print('axis=0: {}'.format(np.mean(meal, axis=0))) # |방향으로 연산
print('axis=1: {}'.format(np.mean(meal, axis=1))) # -방향으로 연산
print()
#=======================================================
#ex2)
#=======================================================
import numpy as np

a = [1, 2, 3, 4]
print(np.mean(a))
print(np.average(a)) #average는 weight라는 것을 줄 수 있음. 
#ex) np.average(a, weights=[1,1,1,2])
print(np.average(a, weights=[1, 1, 1, 2]))
print()