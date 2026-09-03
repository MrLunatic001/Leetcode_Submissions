class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start,comb,currentSum):
            if len(comb) == k:
                if sum(comb) == n:
                    res.append(comb)
                return

            for i in range(start,10):
                if currentSum + i > n:
                    break
                backtrack(i+1,comb + [i], currentSum + i)

        backtrack(1,[],0)

        return res