from src import Hub, Connection


class Graph:
    def __init__(self, hub_list: list[Hub],
                 conn_list: list[Connection]) -> None:
        self.nodes: dict[str, dict[str, int]] = {}
        self.hubs: dict[str, Hub] = {}
        self.start: str = ""
        self.end: str = ""

        cost: dict[str, int] = {}
        for node in hub_list:
            if node.hub_type == "start_hub":
                self.start = node.name
            if node.hub_type == "end_hub":
                self.end = node.name
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
