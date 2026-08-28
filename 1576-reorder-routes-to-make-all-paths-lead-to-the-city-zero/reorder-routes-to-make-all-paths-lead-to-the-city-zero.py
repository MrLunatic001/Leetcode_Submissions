class Solution:
        
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u,v in connections:
            adj[u].append((v,1))
            adj[v].append((u,0))
        ans = 0
        visited = set()

        def dfs(node):
            nonlocal ans
            visited.add(node)

            for nei,c in adj[node]:
                if nei not in visited:
                    ans += c
                    dfs(nei)

        dfs(0)


        return ans


            
