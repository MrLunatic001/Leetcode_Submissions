class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        ans = currentSum

        for i in range(k, len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]
            ans = max(ans, currentSum)

        return ans / k