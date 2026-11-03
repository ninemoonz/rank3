from src import Hub, Connection


class Graph:
    def __init__(self, hub_list: list[Hub],
                 conn_list: list[Connection]) -> None:
        # self.node: dict[str, str] = {}
        # self.link_to: dict[str, list[tuple[str, Connection]]] = {}
        self.graph: dict[str, dict[str, int]] = {}

        cost: dict[str, int] = {}
        for node in hub_list:
            cost[node.name] = node.cost

        for node in hub_list:
            inner: dict[str, int] = {}
            for conn in conn_list:
                if node.name == conn.hub_from:
                    inner[conn.hub_to] = cost[conn.hub_to]
            self.graph[node.name] = inner
        print("[GRAPH]")
        for element in self.graph:
            print(f"Key: {element} | Value: {self.graph[element]}")

        # for hub in hub_list:
        #     self.node[hub.name] = hub
        #     self.link_to[hub.name] = []

        # for conn in conn_list:
        #     self.link_to[conn.hub_from].append((conn.hub_to, conn))
        #     self.link_to[conn.hub_to].append((conn.hub_from, conn))
