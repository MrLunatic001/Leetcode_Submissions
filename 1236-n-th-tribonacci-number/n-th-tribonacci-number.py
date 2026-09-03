class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0,1,1]
        t = deque(t)
        counter = 3
        if n <= 2:
            return t[n]

        while counter <= n:
            temp = sum(t)
            t.popleft()
            t.append(temp)
            counter += 1

        return t[-1]
