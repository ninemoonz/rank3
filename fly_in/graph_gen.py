from src import Hub, Connection


class Graph:
    def __init__(self, hub_list: list[Hub],
                 conn_list: list[Connection]) -> None:
        self.nodes: dict[str, dict[str, int]] = {}
        self.hubs: dict[str, Hub] = {}

        cost: dict[str, int] = {}
        for node in hub_list:
            cost[node.name] = node.cost
            self.hubs[node.name] = node

        for node in hub_list:
            if node.zone == "blocked":
                continue
            self.nodes[node.name] = {}

        for conn in conn_list:
            a = conn.hub_from
            b = conn.hub_to
            if a not in self.nodes or b not in self.nodes:
                continue
            self.nodes[a][b] = cost[b]
            self.nodes[b][a] = cost[a]

        for node in self.nodes:
            print(f"node '{node}': {self.nodes[node]}")
