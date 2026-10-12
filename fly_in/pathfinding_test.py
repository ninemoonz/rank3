from graph_gen import Graph
from src import Drone


class PathFinder:
    def __init__(self, graph_map: Graph, drones: list[Drone]):
        self.graph_map = graph_map
        self.drone = drones
        self.start = graph_map.node["start"]
        self.goal = graph_map.node["goal"]

    def prepare_drones(self) -> None:
        try:
            for drone in self.drones:
                drone.present_hub = self.start
        except ValueError as e:
            print(e)

    def shortest_path(self) -> None:
            