class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        vowels = {'a','e','i','o','u'}
        for c in s:
            if c.lower() in vowels:
                v.append(c)

        ans = ""
        for c in s:
            if c.lower() in vowels:
                ans += v.pop()
            else:
                ans += c
        return ans