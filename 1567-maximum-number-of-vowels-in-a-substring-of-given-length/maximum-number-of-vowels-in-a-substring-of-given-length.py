class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = s.lower()
        ans,currentSum = 0,0
        vowels = {'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowels:
                ans += 1
                currentSum += 1

        
        for i in range(k,len(s)):
            if s[i] in vowels:
                currentSum += 1
            if s[i-k] in vowels:
                currentSum -= 1
            print(currentSum)
            ans = max(ans,currentSum)

        return ans
            


