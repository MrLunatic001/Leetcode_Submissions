class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dpCurr = 0
        dpPrev = 0
        for num in nums:
            tmp = dpCurr
            dpCurr = max(dpPrev + num, dpCurr)
            dpPrev = tmp

        return dpCurr

        
