class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s = s.split()
        s.reverse()
        for word in s:
            ans += word
            ans += " "
        return ans[:len(ans)-1]