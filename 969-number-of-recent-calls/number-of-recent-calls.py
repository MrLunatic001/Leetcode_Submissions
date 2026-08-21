class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        ans = 0
        for i in range(len(self.requests)):
            r = self.requests.popleft()
            if r >= t - 3000 :
                ans += 1
                self.requests.append(r)
        return ans

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)