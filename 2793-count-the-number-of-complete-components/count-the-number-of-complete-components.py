class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        component_freq = defaultdict(int)
        for vertex in range(n):
            graph[vertex] = [vertex]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        for vertex in range(n):
            neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1

        return sum(
            1
            for neighbors, freq in component_freq.items()
            if len(neighbors) == freq
        )

        