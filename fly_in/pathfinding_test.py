from collections import deque
from graph_gen import Graph
from src import Drone


class PathFinder:
    def __init__(self, graph_map: Graph, drones: list[Drone]):
        self.graph_map = graph_map
        self.drones = drones
        self.start = graph_map.node["start"]
        self.goal = graph_map.node["goal"]

    def path_bfs(self) -> list[str]:
        starting_hub = self.start.name
        queue: deque[str] = deque([starting_hub])
        visited: set[str] = {starting_hub}
        past_hub: dict[str, str] = {}
        while queue:
            current: str = queue.popleft()
            for name, linked_hub in self.graph_map.link_to[current]:
                if name not in visited:
                    queue.append(name)
                    visited.add(name)
                    past_hub[name] = current
        if "goal" not in visited:
            return None
        path = ["goal"]
        node = "goal"
        while node != "start":
            node = past_hub[node]
            path.append(node)
        path.reverse()
        return path

    def cost_path(self) -> list[str]:
        starting_hub = self.start
        queue: deque[tuple[str, int]] = deque()
        queue.append((starting_hub.name, starting_hub.cost))
        visited: set[str] = {starting_hub}
        past_hub: dict[str, str] = {}
        while queue:
            item = queue.popleft()
            current, cost = item
            for name, linked_hub in self.graph_map.link_to[current]:
                if name not in visited:
                    queue.append(name)
                    visited.add(name)
                    past_hub[name] = current
        if "goal" not in visited:
            return None
        path = ["goal"]
        node = "goal"
        while node != "start":
            node = past_hub[node]
            path.append(node)
        path.reverse()
        return path
