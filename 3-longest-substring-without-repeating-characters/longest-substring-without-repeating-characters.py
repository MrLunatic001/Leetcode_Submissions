class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        window = set()
        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1

            
            ans = max(ans, right - left + 1)
            window.add(s[right])
        return ans
                
                