def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return merge(left,right)

def merge(left, right):
    result = []
    l = r = 0

    while l < len(left)  and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])

    return result
    
class Solution:
    def sortArray(self, nums):
        return mergeSort(nums)