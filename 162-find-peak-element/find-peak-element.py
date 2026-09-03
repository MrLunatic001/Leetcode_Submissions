class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
 
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Otherwise, a peak exists at mid or to the left
            else:
                right = mid
        return left