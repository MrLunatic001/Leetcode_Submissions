class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.totalSum = sum(nums)
        memo = [
            [float("-inf")] * (2*self.totalSum + 1) for _ in range(len(nums))
        ]

        return self.calculateWays(nums,0,0,target,memo)

    def calculateWays(self,nums,currentIndex,currentSum,target,memo):
        if currentIndex == len(nums):
            return 1 if currentSum == target else 0
        else:
            if memo[currentIndex][currentSum + self.totalSum] != float("-inf"):
                return memo[currentIndex][currentSum + self.totalSum]
            add = self.calculateWays(nums,currentIndex + 1,currentSum + nums[currentIndex],target,memo)
            subtract = self.calculateWays(
                nums,
                currentIndex + 1,
                currentSum - nums[currentIndex],
                target,
                memo,
            )
            memo[currentIndex][currentSum + self.totalSum] = add + subtract
            return memo[currentIndex][currentSum + self.totalSum]