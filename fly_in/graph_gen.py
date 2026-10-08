from src import Hub, Connection


class Graph:
    def __init__(self, hub_list: list[Hub],
                 conn_list: list[Connection]) -> None:
        self.node: dict[str, Hub] = {}
        self.link_to: dict[str, list[tuple[str, Connection]]] = {}

        for hub in hub_list:
            self.node[hub.name] = hub
            self.link_to[hub.name] = []

        for conn in conn_list:
            self.link_to[conn.hub_from].append((conn.hub_to, conn))
            self.link_to[conn.hub_to].append((conn.hub_from, conn))
