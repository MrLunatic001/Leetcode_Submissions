def invert(s):
    ans = ""
    for c in s:
        if c == "0":
            ans += "1"
        else:
            ans += "0"
    return ans
def genStr(n):
    if n == 1:
        return "0"
    else:
        return genStr(n-1) + "1" + invert(genStr(n-1))[::-1]

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = genStr(n)
        return ans[k-1]