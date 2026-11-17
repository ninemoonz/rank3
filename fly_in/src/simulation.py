from src.graph_gen import Graph
from src.class_model import Drone


class Simulation:
    def __init__(
                 self,
                 graph: Graph,
                 drones: list[Drone],
                 path: list[str]
                ) -> None:
        self.graph = graph
        self.drones = drones
        self.path = path
        self.position: dict[int, str] = {}  # drone no. -> hub name

        # debug line
        for drone in self.drones:
            self.position[drone.drone_nb] = self.graph.start
            print(f"drone: {drone.drone_nb}: {self.position[drone.drone_nb]}")
