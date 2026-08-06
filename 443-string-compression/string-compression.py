class Solution:
    def compress(self, chars: List[str]) -> int:
        currChar = chars[0]
        counter = 0

        s = ""

        for c in chars:
            if currChar == c:
                counter += 1
            else:
                s += currChar
                if counter > 1:
                    s += str(counter)
                currChar = c
                counter = 1
        s += currChar
        if counter > 1:
            s += str(counter)
        chars[:len(s)] = s
        return len(s)
        
