class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = [[] for _ in range(n)]
        for f,t,cost in edges:
            self.adj_list[f].append((t,cost))

    def addEdge(self, edge: List[int]) -> None:
        f,t,c = edge
        self.adj_list[f].append((t,c))

    def shortestPath(self, node1: int, node2: int) -> int:
        n = len(self.adj_list)
        pq = [(0,node1)]
        cost = [inf] * (n)
        cost[node1] = 0
        while pq:
            c, node = heappop(pq)
            if c > cost[node]:
                continue
            if node == node2:
                return c
            for neigh, neighCost in self.adj_list[node]:
                newCost = c + neighCost
                if newCost < cost[neigh]:
                    cost[neigh] = newCost
                    heappush(pq,(newCost,neigh))

        return -1
            


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)