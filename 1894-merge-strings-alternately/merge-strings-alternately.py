class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        end = min(len(word1),len(word2))
        for i in range(end):
            ans += word1[i]
            ans += word2[i]

        if len(word1) > len(word2):
            ans += word1[end:]
        elif len(word2) > len(word1):
            ans += word2[end:]

        return ans