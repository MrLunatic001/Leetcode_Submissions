def mergeSort(nums):
    if len(nums) <= 1:
        return nums,0

    mid = len(nums) // 2

    left,lc = mergeSort(nums[:mid])
    right,rc = mergeSort(nums[mid:])
    c = lc + rc

    j = 0
    for i in range(len(left)):
        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        c += j




    return merge(left,right),c

def merge(left,right):
    nums = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums.append(left[i])
            i += 1
        else:
            nums.append(right[j])
            j += 1

    nums.extend(left[i:])
    nums.extend(right[j:])

    return nums

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return mergeSort(nums)[1]