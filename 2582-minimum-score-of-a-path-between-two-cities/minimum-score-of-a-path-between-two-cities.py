class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b,dist in roads:
            graph[a].append((b,dist))
            graph[b].append((a,dist))
        visited = set()
        def dfs(node):
            visited.add(node)
            for v,d in graph[node]:
                self.min_dist = min(self.min_dist,d)
                if v not in visited:
                    dfs(v)


        
        self.min_dist = float('inf')
        dfs(1)
        return self.min_dist
