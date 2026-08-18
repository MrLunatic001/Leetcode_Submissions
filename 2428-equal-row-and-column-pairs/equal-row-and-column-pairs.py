class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        ans = 0
        for j in range(n):
            col = []
            for i in range(n):
                col.append(grid[i][j])
            ans += rows[tuple(col)]
        return ans
        