from collections import deque
from graph_gen import Graph
from src import Drone


class PathFinder:
    def __init__(self, graph_map: Graph, drones: list[Drone]):
        self.graph_map = graph_map
        self.drones = drones
        self.start = graph_map.node["start"]
        self.goal = graph_map.node["goal"]

    def prepare_drones(self) -> None:
        for drone in self.drones:
            drone.present_hub = self.start

    def path_bfs(self) -> None:
        queue = deque(["start"])
        visited = {"start"}
        past_hub = {}
        while queue:
            current = queue.popleft()
            print(current)
            for name, _ in self.graph_map.link_to[current]:
                if name not in visited:
                    queue.append(name)
                    visited.add(name)
                    past_hub[name] = current
        print(f"PARENTS: {past_hub}")
        if "goal" not in visited:
            return None
        path = ["goal"]
        node = "goal"
        while node != "start":
            node = past_hub[node]
            path.append(node)
        path.reverse()
        print(path)
