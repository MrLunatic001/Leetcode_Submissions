class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        found = False
        for char in s[::-1]:
            if char == " ":
                if found:
                    return ans
            else:
                found = True
                ans += 1

        return ans