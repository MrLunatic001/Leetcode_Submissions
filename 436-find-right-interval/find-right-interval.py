class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # (start, original index)
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        ans = []

        for start, end in intervals:
            # Find the first interval whose start >= end
            idx = bisect_left(starts, (end,))

            if idx == len(starts):
                ans.append(-1)
            else:
                ans.append(starts[idx][1])

        return ans