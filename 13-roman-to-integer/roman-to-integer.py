class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            cur = m[char]
            if cur < prev_value:
                total -= cur
            else:
                total += cur

            prev_value = cur

        return total