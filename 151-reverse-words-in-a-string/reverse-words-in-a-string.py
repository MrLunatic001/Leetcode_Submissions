class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        start = True
        space_counter = 0
        temp = ""
        for char in s[::-1]:

            if char == " ":
                if not start and space_counter < 1:
                    ans += temp[::-1]
                    temp = ""
                    ans += char
                    space_counter += 1

            else:
                space_counter = 0
                start = False
                temp += char

        if space_counter == 0 and temp != "":
            ans += temp[::-1]
        if ans[-1] == " ":
            ans = ans[0:len(ans)-1]
        return ans

