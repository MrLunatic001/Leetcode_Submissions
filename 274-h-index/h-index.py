class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0