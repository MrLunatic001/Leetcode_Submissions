class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        G1 = defaultdict(list)
        G2 = defaultdict(list)
        for a,b,w in edges:
            G1[a].append((b,w))
            G2[b].append((a,w))

        def Dijkstra(graph,K):
            q,t = [(0,K)],{}
            while q:
                time,node = heappop(q)
                if node not in t:
                    t[node] = time
                    for v,w in graph[node]:
                        heappush(q,(time+w,v))
            result = []
            for i in range(n):
                result.append(t.get(i, float("inf")))

            return result

        arr1 = Dijkstra(G1,src1)
        arr2 = Dijkstra(G1,src2)
        arr3 = Dijkstra(G2,dest)
        ans = float("inf")

        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])

        return ans if ans != float("inf") else -1