#=============================================================================
# merge_sort 방식
# # buble_sort...처음부터 끝까지 아이템을 보고 그 다음 아이템과 비교해서 크면 뒤로 보내기
#=============================================================================
def bubble_sort(nums) :
    for i in range(len(nums), 0, -1):
        for j in range(i-1):
            if nums[j] > nums[j+1]:
                t = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = t
    return nums

from random import shuffle
from time import time
arr = list(range(30000))
shuffle(arr)

start = time()
answer = bubble_sort(arr)
end = time()

print('time = {}'.format(end-start))
print()


#=============================================================================
# merge_sort 방식
#=============================================================================
def merge_sort(nums):
    nums = [[num] for num in nums]
    semi_sorted = []
    def sort_two_array(arr1, arr2):
        answer = []
        while len(arr1) !=0 or len(arr2) !=0:
            if len(arr1) ==0: answer.append(arr2.pop(0))
            elif len(arr2) ==0: answer.append(arr1.pop(0))
            elif arr1[0] < arr2[0] : answer.append(arr1.pop(0))
            elif arr1[0] >= arr2[0]: answer.append(arr2.pop(0))
        return answer
    while len(nums) != 1:
        for i in range(0, len(nums), 2):
            if i == len(nums)-1: semi_sorted.append(nums[i])
            else : semi_sorted.append(sort_two_array(nums[i], nums[i+1]))
        nums = semi_sorted
        semi_sorted = []
    return nums[0]
from random import shuffle
from time import time
arr = list(range(30000))
shuffle(arr)

start=time()
answer = merge_sort(arr)
end=time()

print('time={}'.format(end-start))