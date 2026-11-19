from src.class_model import Drone
from src.graph_gen import Graph


class Simulation:
    def __init__(self,
                 graph: Graph, drones: list[Drone], path: list[str]) -> None:
        self.graph = graph
        self.drones = drones
        self.path = path
        self.position: dict[int, str] = {}

        for drone in self.drones:
            self.position[drone.drone_nb] = self.graph.start

    def one_turn(self) -> None:
        ...