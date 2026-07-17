class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ans = 0
        if len(nums) <= 0:
            return ans
        elif len(nums) == 1:
            return 1
      

        even = [nums[0]]
        evenCounter = 1
        odd = [nums[1]]
        oddCounter = 1
        for i in range(2,len(nums)):
            if i % 2 == 0:
                even.append(even[evenCounter - 1] + nums[i])
                evenCounter += 1
            else:
                odd.append(odd[oddCounter - 1] + nums[i])
                oddCounter += 1
        print(even)
        print(odd)
        for i in range(len(nums)):
            if i % 2 == 0:
                evenInd = int(i/2)
                if evenInd > 0:
                    evenTotal = even[evenInd-1] + odd[-1] - odd[evenInd-1]
                    oddTotal = odd[evenInd-1] + even[-1]-even[evenInd]
                else:
                    evenTotal = odd[-1]
                    oddTotal = even[-1] - even[0]
            else:
                oddInd = floor(i/2)
                if oddInd > 0:
                    oddTotal = odd[oddInd-1] + even[-1] - even[oddInd]
                    evenTotal = even[oddInd] + odd[-1] - odd[oddInd]
                else:
                    oddTotal = even[-1] - even[0]
                    evenTotal = even[0] + odd[-1] - odd[0]
            if oddTotal == evenTotal:
                ans += 1
        return ans

        