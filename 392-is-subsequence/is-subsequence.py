class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        if s == "":
            return True
        for char in t:
            if s[counter] == char:
                counter += 1
                if counter == len(s) :
                    return True

        if counter == len(s) :
            return True
        return False
        