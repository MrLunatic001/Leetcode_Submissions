class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        counter = 0

        for c in t:
            if c == s[counter]:
                counter += 1
                if counter >= len(s):
                    return True
        
        return False
        