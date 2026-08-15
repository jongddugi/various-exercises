def is_prime(num):
    if num <= 1 : return False
    for i in range(2, int(num **(1/2))+1):
        if num % i ==0:
            return False
    return True

nums = [i+1 for i in range(30)]
primes = []
for i in nums:
    if is_prime(i) : 
        primes.append(i)
print(primes)
print()

nums = [i+1 for i in range(30)]
primes = list(filter(is_prime, nums))
print(primes)
print()

# filter(function, list)
# function : 거르는 기준이 되는 함수
# list : 걸러질 리스트

nums = [i+1 for i in range(30)]
primes = [i for i in nums if is_prime(i)]
print(primes)
print()
#이렇게 리스트를 넣어주고 if로 조건 걸어줘도 가능함.