from heapq import heapify, heappop, heappush
from graph_gen import Graph


class Dijkstra:
    def __init__(self, graph: Graph):
        self.graph = graph

    # def add_edge(self, node1, node2, weight):
    #     if node1 not in self.graph:
    #         self.graph[node1] = {}
    #     self.graph[node1][node2] = weight

    def shortest_distances(self,
                           source: str = "start",
                           target: str = "goal") -> dict[str, float]:
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph.node}
        distances[source] = 0

        # initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visted nodes
        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue  # Skip already visited nodes
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                distance_so_far = current_distance + weight
                if distance_so_far < distances[neighbor]:
                    distances[neighbor] = distance_so_far
                    heappush(pq, (distance_so_far, neighbor))
        predecessors = {node: None for node in self.graph}

        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        path = []
        current_node = target

        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        path.reverse()
        return path
