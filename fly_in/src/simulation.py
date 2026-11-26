from src.class_model import Drone
from src.graph_gen import Graph


class Simulation:
    def __init__(self,
                 graph: Graph, drones: list[Drone], path: list[str]) -> None:
        self.graph = graph
        self.drones = drones
        self.path = path
        self.position: dict[str, str] = {}  # drone_name: hub_name
        self.in_transit: dict[str, str] = {}  # drone_name: next_hub

        for drone in self.drones:
            self.position[drone.drone_nb] = self.graph.start

    def one_turn(self) -> None:
        """
        one_turn method will implement the movement of drone in one turn.
        this method will be repeated until all the drones reach the goal.
        this method is implemented in run method.
        """
        moves: list[str] = []
        drone_cross: dict[frozenset[str], int] = {}
        for drone in self.drones:
            current_hub = self.position[drone.drone_nb]
            # checks if the drone arrived to the final destination
            if current_hub == self.graph.end:
                continue
            path_index = self.path.index(current_hub)
            next_hub = self.path[path_index + 1]
            # from link to next hub for restricted zone case
            if drone.drone_nb in self.in_transit.keys():
                link_key = frozenset((current_hub, next_hub))
                if link_key not in drone_cross:
                    drone_cross[link_key] = 0
                drone_cross[link_key] += 1
                self.position[drone.drone_nb] = next_hub
                self.in_transit.pop(drone.drone_nb)
                landing: str = drone.drone_nb + "-" + next_hub
                moves.append(landing)
                continue
            # drone counting
            drone_count: int = 0
            for name, hub in self.position.items():
                if name in self.in_transit:
                    continue
                if hub == next_hub:
                    drone_count += 1
            for transit in self.in_transit.values():
                if transit == next_hub:
                    drone_count += 1
            drone_limit: int = self.graph.hubs[next_hub].max_drones
            if drone_count >= drone_limit:
                continue
            # connection check
            link_key = frozenset((current_hub, next_hub))
            if link_key not in drone_cross:
                drone_cross[link_key] = 0
            link_limit: int = self.graph.links[link_key].max_link_capacity
            if drone_cross[link_key] >= link_limit:
                continue
            # zone restriction check
            zone_type: str = self.graph.hubs[next_hub].zone
            transit_link: str = (current_hub + "-" + next_hub)
            if zone_type == "restricted":
                self.in_transit[drone.drone_nb] = next_hub
                drone_cross[link_key] += 1
                moves.append(drone.drone_nb + "-" + transit_link)
                continue
            self.position[drone.drone_nb] = next_hub
            drone_cross[link_key] += 1
            drone_move: str = drone.drone_nb + "-" + next_hub
            moves.append(drone_move)
        result = " ".join(moves)
        print(result)

    def run(self) -> None:
        """
        run method is a loop which will keep going until all the drones arrive.
        """
        turn_counter: int = 0
        while not self.all_arrived():
            self.one_turn()
            turn_counter += 1
        print(f"turn: {turn_counter}")

    def all_arrived(self) -> bool:
        """
        all_arrived method will check if all the drones arrived to goal or not.
        """
        finished: int = 0
        finished_number = len(self.position)
        for value in self.position.values():
            if value == self.graph.end:
                finished += 1
        return (finished_number == finished)
