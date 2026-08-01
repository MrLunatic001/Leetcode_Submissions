class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)

        for i, route in enumerate(routes):
            for stops in route:
                graph[stops].append(i)
        
        q = deque()
        visited = set()

        for route in graph[source]:
            q.append(route)
            visited.add(route)

        busCount = 1


        while q:
            size = len(q)
            for i in range(size):
                route = q.popleft()

                for stop in routes[route]:
                    if stop == target:
                        return busCount

                    for nextRoute in graph[stop]:
                        if nextRoute not in visited:
                            visited.add(nextRoute)
                            q.append(nextRoute)

            busCount += 1

        return -1