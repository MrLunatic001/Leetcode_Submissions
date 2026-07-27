class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def dfs():
            nonlocal i
            ans = ""

            while i < len(s) and s[i] != "]":
                if s[i].isalpha():
                    ans += s[i]
                    i += 1
                else:
                    # Read the full number
                    k = 0
                    while s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1

                    i += 1          # Skip '['
                    decoded = dfs() # Decode inside brackets
                    i += 1          # Skip ']'

                    ans += decoded * k

            return ans

        return dfs()