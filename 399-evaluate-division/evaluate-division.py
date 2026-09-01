class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.g = defaultdict(list)
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            val = values[i]

            self.g[a].append((b,val))
            self.g[b].append((a,1/val))
        ans = []
        
        for q in queries:
            start = q[0]
            target = q[1]
            self.visited = set()
            ans.append(self.search(start,target,1))
        return ans
    def search(self,start,target,val):
        if target not in self.g or start not in self.g:
            return float(-1.0)
        if start == target:
            return float(1.0)
        self.visited.add(start)
        for n in self.g[start]:
            if n[0] not in self.visited:
                res = self.search(n[0],target,val)
                if res != -1.0:
                    return res * n[1]
        return float(-1.0)

