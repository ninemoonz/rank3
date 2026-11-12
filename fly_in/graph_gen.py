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
            inner: dict[str, int] = {}
            if node.zone == "blocked":
                continue
            for conn in conn_list:
                if node.name == conn.hub_from:
                    inner[conn.hub_to] = cost[conn.hub_to]
            self.nodes[node.name] = inner
