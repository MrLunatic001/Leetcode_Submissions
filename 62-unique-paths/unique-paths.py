class Solution:
    def uniquePaths(self, m: int, n: int, i = 0, j = 0) -> int:
        dp = []
        for i in range(2):
            row = []
            for j in range(n):
                row.append(1)
            dp.append(row)

        # Alternating row DP logic using modulo (% 2) instead of bitwise (& 1)
        for i in range(1, m):
            for j in range(1, n):
                dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]
                
        return dp[(m - 1) % 2][-1]

