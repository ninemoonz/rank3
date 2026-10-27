from collections import deque
from graph_gen import Graph
from src import Drone


class PathFinder:
    def __init__(self, graph_map: Graph, drones: list[Drone]):
        self.graph_map = graph_map
        self.drones = drones
        self.start = graph_map.node["start"]
        self.goal = graph_map.node["goal"]

    # def path_bfs(self) -> None:
    #     queue: deque[str] = deque(["start"])
    #     visited: set[str] = {"start"}
    #     past_hub: dict[str, str] = {}
    #     while queue:
    #         current: str = queue.popleft()
    #         for name, _ in self.graph_map.link_to[current]:
    #             if name not in visited:
    #                 queue.append(name)
    #                 visited.add(name)
    #                 past_hub[name] = current
    #     if "goal" not in visited:
    #         return None
    #     path = ["goal"]
    #     node = "goal"
    #     while node != "start":
    #         node = past_hub[node]
    #         path.append(node)
    #     path.reverse()
    #     print(f"Shortest Path: {path}")
    def path_bfs(self) -> None:
        starting = self.start
        frontier: deque[str] = []
        frontier.append(starting.name)
        reached: set[str] = set()
        reached.add(starting.name)
        print(f"frontier: {frontier}")
        print(f"reached: {reached}")
        while len(frontier) > 0:
            for next in self.graph_map.link_to[starting.name]:
                if next not in reached:
                    print(next)
                    frontier.put(next)
                    reached.add(next)
        print(frontier)
        print(reached)
