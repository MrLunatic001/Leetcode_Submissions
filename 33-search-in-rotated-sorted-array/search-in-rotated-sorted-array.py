class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = (s+e) // 2
            if nums[mid] == target:
                return mid

            if nums[s] <= nums[mid]:          # left half sorted
                if nums[s] <= target < nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:                             # right half sorted
                if nums[mid] < target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1

        return -1


        