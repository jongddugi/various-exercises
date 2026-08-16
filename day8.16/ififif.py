# if 0+1j:
#     print("0+1j : True!")
# else:
#     print("0+1j : False")
# print(True or 9/0)
# print(True and 9/0)

#=======================================================
# if숫자
#=======================================================
if 1 :
    print('hello')
if -1 :
    print('hello')
if 1 :
    print('hello')
if  0:
    print('hello')
else:
    print('hi')

print()
print()
# 숫자는 0말고는 if문에서 다 true로 취급

#=======================================================
# if리스트
#=======================================================
print('list')
if [1, 2, 3]:
    print('hello')
else:
    print('hi')

if []:
    print(hello)
else: 
    print('hi')
print()


#=======================================================
# if리스트 하수버전
#=======================================================
print('list_low')
arr = [3, 2, 1]

for i in range(10):
    if arr ==[]:
        break
    else:
        arr.pop(0)
    print('arr: {}'.format(arr))
print('last arr: {}'.format(arr))
print()

#=======================================================
# if리스트 고수버전
#=======================================================
print('list_high')
arr = [3, 2, 1]

for i in range(10):
    if arr :
        arr.pop(0)
    else: 
        break
    print('arr: {}'.format(arr))
print('last arr: {}'.format(arr))


#short circuit evaluation
#논리 계산에서 앞을 보면 뒤를 볼 필요가 없을 때 뒤의 계산 자체를 수행하지 않는 것