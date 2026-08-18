class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = defaultdict(int)
        for num in arr:
            occur[num] += 1

        check = set()

        for o in occur.values():
            if o not in check:
                check.add(o)
            else:
                return False
        return True