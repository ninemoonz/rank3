from collections import deque
from graph_gen import Graph
from src import Drone


class PathFinder:
    def __init__(self, graph_map: Graph, drones: list[Drone]):
        self.graph_map = graph_map
        self.drones = drones
        self.start = graph_map.node["start"]
        self.goal = graph_map.node["goal"]

    # def path_bfs(self) -> list[str]:
    #     starting_hub = self.start.name
    #     queue: deque[str] = deque([starting_hub])
    #     visited: set[str] = {starting_hub}
    #     past_hub: dict[str, str] = {}
    #     while queue:
    #         current: str = queue.popleft()
    #         for name, linked_hub in self.graph_map.link_to[current]:
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
    #     return path

    def cost_path(self) -> list[str]:
        starting_hub = self.start
        
        queue: deque[tuple[str, int]] = deque()
        queue.append((starting_hub.name, starting_hub.cost))
        past_hub: dict[str, str] = {}
        cost_list: dict[str, int]= {}
        cost_list[starting_hub.name] = 0
        while queue:
            item = queue.popleft()
            current, cost = item
            for next, _ in self.graph_map.link_to[current]:
                new_cost = cost + self.graph_map.node[next].cost
                if next not in cost_list or new_cost < cost_list[next]:
                    cost_list[next] = new_cost
                    queue.append((next, new_cost))
                    past_hub[next] = current
                turn += 1
        path = ["goal"]
        node = "goal"
        while node != "start":
            node = past_hub[node]
            path.append(node)
        path.reverse()
        return path
