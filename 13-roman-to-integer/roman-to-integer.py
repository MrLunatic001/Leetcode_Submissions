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
        ans = 0
        
        s = list(s)
        prev = s[0]
        for i in range(len(s)):
            cur = s[i]
            if m[cur] <= m[prev]:
                ans += m[cur]
            else:
                ans -= m[prev]
                ans += m[cur] - m[prev]

            prev = cur



        return ans