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
        for drone in self.drones:
            current_hub = self.position[drone.drone_nb]  # current_hub = start
            path_index = self.path.index(current_hub)  # path_index = 0
            next_hub = self.path[path_index + 1]  # next_hub = waypoint1
            drone_count: int = 0
            for hub in self.position.values():  # [start, start]
                if hub == next_hub:
                    drone_count += 1
            drone_limit: int = self.graph.hubs[next_hub].max_drones
            if drone_count >= drone_limit:
                continue
            self.position[drone.drone_nb] = next_hub  # {D1: 'waypoint1', D2: 'start'}
        print(self.position)
