class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for _ in range(len(nums)):
            if nums[counter] == 0:
                
                nums[:] = nums[:counter] + nums[counter + 1:] + [0]
            else:
                counter += 1
                

                


        
        