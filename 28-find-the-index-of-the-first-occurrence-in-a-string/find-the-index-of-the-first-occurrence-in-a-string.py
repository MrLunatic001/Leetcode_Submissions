class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i = 0
        for i in range(len(haystack) - n + 1):
            if needle == haystack[i:i+n]:
                return i

        return -1

