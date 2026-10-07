from .class_model import Drone, Hub, Connection
from .config_parsing import HubData, ConnData


class DronesFactory:
    def make_drones(self, drone_info: int) -> list[Drone]:
        drone_list: list[Drone] = []
        for i in range(drone_info):
            new_drone = Drone(drone_nb=i)
            drone_list.append(new_drone)
        return drone_list


class HubsFactory:
    def make_hubs(self,
                  hub_info: tuple[HubData, ...],
                  drones: int) -> list[Hub]:
        hub_list: list[Hub] = []
        for hub in hub_info:
            hub_type: str = hub[0]
            hub_name: str = hub[1]
            hub_coord: tuple[int, int] = hub[2]
            meta_dict: dict[str, str] = hub[3]
            new_hub = Hub.model_validate({"hub_type": hub_type,
                                          "name": hub_name,
                                          "coord": hub_coord,
                                          **meta_dict})
            if hub_type in ("start_hub", "end_hub"):
                new_hub.max_drones = drones
            hub_list.append(new_hub)
        return hub_list


class ConnectionsFactory:
    def make_connections(self,
                         conn_info: tuple[ConnData, ...]) -> list[Connection]:
        conn_list: list[Connection] = []
        for conn in conn_info:
            conn_from: str = conn[0]
            conn_to: str = conn[1]
            meta_dict: dict[str, str] = conn[2]
            new_conn = Connection.model_validate({"hub_from": conn_from,
                                                  "hub_to": conn_to,
                                                  **meta_dict})
            conn_list.append(new_conn)
        return conn_list
