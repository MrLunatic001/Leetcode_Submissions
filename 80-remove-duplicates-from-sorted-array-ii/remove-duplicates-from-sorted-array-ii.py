class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ans = 1
        counter = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[ans-1]:
                nums[ans] = nums[i]
                ans += 1
                counter = 1
            elif counter < 2:
                nums[ans] = nums[i]
                ans += 1
                counter += 1
            
        return ans