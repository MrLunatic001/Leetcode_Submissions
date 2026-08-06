class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product = 1
        numZero = 0
        nonZero = 1
        for num in nums:
            product *= num
            if num == 0:
                numZero += 1
            else:
                nonZero *= num

        for num in nums:
            if num == 0:
                if numZero == 1:
                    answer.append(nonZero)
                else:
                    answer.append(0)
            else:
                answer.append(product//num)
        return answer