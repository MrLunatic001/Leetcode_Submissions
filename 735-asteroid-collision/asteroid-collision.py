class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while ans and ans[-1] > 0 and a < 0:
                diff = a + ans[-1]
                if diff < 0:
                    ans.pop()
                elif diff > 0:
                    a = 0
                else:
                    ans.pop()
                    a = 0
            if a:
                ans.append(a)

        return ans