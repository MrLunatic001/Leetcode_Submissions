class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        have = set()

        for i in range(len(nums)):
            if nums[i] not in have:
                have.add(nums[i])
                nums[ans] = nums[i]
                ans += 1

        return ans