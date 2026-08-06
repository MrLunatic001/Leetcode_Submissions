class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        ans = []
        for candy in candies:
            if candy + extraCandies >= most:
                ans.append(True)
            else:
                ans.append(False)

        return ans