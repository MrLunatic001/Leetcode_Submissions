class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        current_max = nums[0]
        for i in range(len(nums)):
            current_max = max(current_max, nums[i])
            prefixGcd.append(gcd(nums[i],current_max))

        prefixGcd.sort()
        sum = 0
        for i in range(floor(len(prefixGcd)/2)):
            sum += gcd(prefixGcd[i],prefixGcd[len(prefixGcd)-1-i])
        return sum