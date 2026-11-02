from heapq import heapify, heappop, heappush

graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
}


class Graph:
    def __init__(self, graph: dict[str, dict[str, int]]):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str) -> dict[str, float]:
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
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
                print(f"neighbor: {neighbor} | weight: {weight}")
                distance_so_far = current_distance + weight
                if distance_so_far < distances[neighbor]:
                    distances[neighbor] = distance_so_far
                    heappush(pq, (distance_so_far, neighbor))

        return distances


if __name__ == "__main__":
    G = Graph(graph)

    distances = G.shortest_distances("B")
    to_F = distances["F"]
    print(f"The shortest distance from B to F is {to_F}")