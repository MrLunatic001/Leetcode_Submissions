class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        prefix = 0
        ans = len(nums)
        seen = {0: -1}

        for i, x in enumerate(nums):
            prefix = (prefix + x) % p

            need = (prefix - target) % p

            if need in seen:
                ans = min(ans, i - seen[need])

            seen[prefix] = i

        return ans if ans < len(nums) else -1