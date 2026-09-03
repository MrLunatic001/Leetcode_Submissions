class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed mid
            # math.ceil(p / mid) is equivalent to (p + mid - 1) // mid
            total_hours = 0
            for p in piles:
                total_hours += (p + mid - 1) // mid
            
            if total_hours <= h:
                # mid speed is fast enough; try to find a smaller valid speed
                right = mid
            else:
                # mid speed is too slow; increase speed
                left = mid + 1
                
        return left
