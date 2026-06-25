from collections import deque
class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        queue = deque([(source,0)])
        visited_bus = [False] * len(routes)
        visited_station = set()

        station_graph = {}
        for idx, bus in enumerate(routes):
            for station in bus:
                if not station_graph.get(station):
                    station_graph[station] = []

                station_graph[station].append(idx)

        visited_station.add(source)

        while queue:
            stop, count = queue.popleft()

            bus_list = station_graph.get(stop, [])
            
            for bus in bus_list:
                if visited_bus[bus]:
                    continue

                bus_routes = routes[bus]
                for route in bus_routes:

                    if route == target:
                        return count + 1
                    if route in visited_station:
                        continue
                    visited_bus[bus] = True
                    visited_station.add(route)
                    queue.append((route, count + 1))

        return -1