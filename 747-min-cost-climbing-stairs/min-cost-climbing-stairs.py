class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def minCost(cost,n):
            if (n<0):
                return 0
            if n == 0 or n == 1:
                return cost[n]

            if n in memo:
                return memo[n]

            memo[n] = cost[n] + min(minCost(cost,n-1),minCost(cost,n-2))
            return memo[n]

        return min(minCost(cost,n-1),minCost(cost,n-2))

        