class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [int] * (n+1)

        def findOnes(i):
            counter = 0
            tempi = i
            if i == 0:
                return 0
            power = 0
            while pow(2,power) <= i:
                power += 1
            

            for i in range(power,-1,-1):
                if pow(2,i) <= tempi:
                    tempi -= pow(2,i)
                    counter += 1
                if tempi == 0:
                    break

            return counter
        
        for i in range(n+1):
            ans[i] = findOnes(i)

        return ans

        