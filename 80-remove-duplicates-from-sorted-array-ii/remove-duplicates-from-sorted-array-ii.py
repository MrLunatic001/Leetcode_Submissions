class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ans = 0
        for num in nums:
            if ans < 2 or num != nums[ans - 2]:
                nums[ans] = num
                ans += 1
            
        return ans