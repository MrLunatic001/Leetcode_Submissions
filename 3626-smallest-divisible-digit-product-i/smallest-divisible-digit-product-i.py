class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        found = False
        while not found:
            strN = str(n)
            temp = 1
            for c in strN:
                temp *= int(c)
            if temp % t == 0:
                found = True
                return n
            n += 1
        return n