class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        currentSum = 0
        for i in range(len(nums)):
            if currentSum == totalSum - nums[i]:
                return i
            currentSum += nums[i]
            totalSum -= nums[i]
        return -1