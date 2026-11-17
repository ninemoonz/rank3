from heapq import heapify, heappop, heappush
from graph_gen import Graph


class Dijkstra:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph.nodes
        self.start = graph.start
        self.end = graph.end

    def shortest_distances(self) -> list[str]:
        # Initialize the values of all nodes with infinity
        distances: dict[str, float] = {}
        for node in self.graph:
            distances[node] = float("inf")
        distances[self.start] = 0
        # initialize a priority queue
        pq: list[tuple[float, str]] = [(0, self.start)]
        heapify(pq)

        # Create a set to hold visted nodes
        visited: set[str] = set()

        while pq:
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                distance_so_far = current_distance + weight
                if distance_so_far < distances[neighbor]:
                    distances[neighbor] = distance_so_far
                    heappush(pq, (distance_so_far, neighbor))

        if distances[self.end] == float("inf"):
            raise ValueError(f"No path from {self.start} to {self.end}")
        predecessors: dict[str, str | None] = ({node: None for
                                                node in self.graph})

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        path: list[str] = []
        step: str | None = self.end
        while step:
            path.append(step)
            step = predecessors[step]
        path.reverse()
        return path
