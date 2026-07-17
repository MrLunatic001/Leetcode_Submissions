class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        prefix = {0:-1}
        sum = 0
        
        for i,num in enumerate(nums):
            sum += num
            remainder = sum % k

            if remainder in prefix:
                if i - prefix[remainder] >= 2:
                    return True
            else:
                prefix[remainder] = i
        return False
            