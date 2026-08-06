class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        big,small = "", ""
        ans = ""
        if len(str1) > len(str2):
            big = str1
            small = str2
        else:
            big = str2
            small = str1

        for i in range(len(small)):
            temp = small[:i+1]
            if len(big) % len(temp) == 0 and len(small) % len(temp) == 0:
                tempBig = temp * (len(big) // len(temp))
                tempSmall = temp * (len(small) // len(temp))
                if tempBig == big and tempSmall == small and len(temp) > len(ans):
                    ans = temp
        return ans

        