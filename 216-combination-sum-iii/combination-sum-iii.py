class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start: int, comb: List[int], current_sum: int):
            # Base cases: stop early if combination exceeds length k or target sum n
            if len(comb) == k:
                if current_sum == n:
                    res.append(list(comb))
                return
            
            # Explore numbers from 'start' to 9 to ensure strictly increasing order
            for i in range(start, 10):
                if current_sum + i > n:
                    break  # Prune search space if adding 'i' exceeds target sum
                
                backtrack(i + 1, comb + [i], current_sum + i)
                
        backtrack(1, [], 0)

        return res