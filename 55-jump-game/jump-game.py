class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i, jump in enumerate(nums):
            # If the current index is beyond the furthest reachable point, stop
            if i > max_reach:
                return False
            
            # Update the max index reachable from here
            max_reach = max(max_reach, i + jump)
            
            # Early return if we can already reach or exceed the last index
            if max_reach >= len(nums) - 1:
                return True
                
        return True