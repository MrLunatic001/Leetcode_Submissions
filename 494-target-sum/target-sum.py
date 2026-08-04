class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        dp = []
        for _ in range(len(nums)):
            dp.append([0]*(2*totalSum+1))
        dp[0][nums[0] + totalSum] = 1
        dp[0][-nums[0] + totalSum] += 1
        for i in range(1,len(nums)):
            for sumVal in range(-totalSum,totalSum + 1):
                if dp[i-1][sumVal + totalSum] > 0:
                    dp[i][sumVal + totalSum + nums[i]] += dp[i-1][sumVal+totalSum]
                    dp[i][sumVal + totalSum - nums[i]] += dp[i-1][sumVal + totalSum]

        if abs(target) > totalSum:
            return 0
        else:
            return dp[len(nums)-1][target + totalSum]