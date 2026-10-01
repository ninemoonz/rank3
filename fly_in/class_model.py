from pydantic import BaseModel, Field, model_validator
from typing import Optional


class Drone(BaseModel):
    drone_nb: int = Field(ge=0)
    before_hub: tuple[str, tuple[int, int]]
    present_hub: tuple[str, tuple[int, int]]
    next_hub: tuple[str, tuple[int, int]]


class Hub(BaseModel):
    name: str = Field(min_length=1)
    coord: tuple[int, int]
    zone: Optional[str] = Field(default="normal")
    color: Optional[str] = Field(default=None)
    max_drones: Optional[int] = Field(default=1)

    @model_validator(mode='after')
    def hub_validation(self) -> 'Hub':
        for ch in self.name:
            if ch == '-' or ch == ' ':
                raise ValueError("Not dash or space in a hub name.")
        return self

    def describe(self) -> None:
        print("[Description]")
        print(f"hub name: {self.name}")
        print(f"coordinate: {self.coord}")
        print(f"[metadata]\n"
              f"- zone: {self.zone}\n"
              f"- color: {self.color}\n"
              f"- max drones: {self.max_drones}\n")


class Connection(BaseModel):
    hub_from: str
    hub_to: str
    max_link_capacity: Optional[int] = Field(default=1)

    @model_validator(mode='after')
    def conn_validator(self) -> 'Connection':
        for ch in self.hub_from:
            if ch == '-' or ch == ' ':
                raise ValueError("No dash or space in a hub name. "
                                 f"{self.hub_from}")
        for ch in self.hub_to:
            if ch == '-' or ch == ' ':
                raise ValueError("No dash or space in a hub name. "
                                 f"{self.hub_to}")
        if self.max_link_capacity < 0:
            raise ValueError("Max link capacity should be positive number. "
                             f"{self.max_link_capacity}")
        return self

    def describe(self) -> None:
        print("[Description]")
        print(f"Connection from: {self.hub_from}")
        print(f"Connection to: {self.hub_to}")
        print(f"Max link capacity: {self.max_link_capacity}\n")


class HubsFactory:
    def make_hubs(self, hub_info: tuple[str, ...]) -> list[Hub]:
        hub_list: list[Hub] = []
        for hub in hub_info:
            hub_name: str = hub[0]
            hub_coord: tuple[int, int] = hub[1]
            if len(hub) > 2:
                meta_dict: dict[str, str] = hub[2] or {}
            else:
                meta_dict = {}
            new_hub = Hub(name=hub_name,
                          coord=hub_coord,
                          **meta_dict)
            hub_list.append(new_hub)
        return hub_list


class ConnectionsFactory:
    def make_connections(self, connection_info: tuple[str, ...]) -> list[Connection]:
        conn_list: list[Connection] = []
        for conn in connection_info:
            conn_from: str = conn[0]
            conn_to: str = conn[1]
            if len(conn) > 2:
                meta_dict: dict[str, str] = conn[2] or {}
            else:
                meta_dict = {}
            new_conn = Connection(hub_from=conn_from,
                                  hub_to=conn_to,
                                  **meta_dict)
            conn_list.append(new_conn)
        return conn_list


# class Hub:
#     def __init__(self,
#                  name: str,
#                  coord: tuple[int, int],
#                  metadata: dict[str, str | int] | None) -> None:
#         self.name = name
#         self.coord = coord
#         self.zone: Optional[str] = metadata["zone"]
#         self.color: Optional[str] = metadata["color"]
#         self.max_drones: Optional[int] = metadata["max_drones"]

#     def describe(self) -> None:
#         print(f"hub name: {self.name}")
#         print(f"coordinate: {self.coord}")
#         print(f"metadata:\n"
#               f"zone: {self.zone}\n"
#               f"color: {self.color}\n"
#               f"max drones: {self.max_drones}")


# class HubsFactory:
#     def make_hub(self, hub_info: list[str]) -> list[Hub]:
#         hub_list: list[Hub] = []
#         for hub in hub_info:
#             hub_name: str = hub[0]
#             try:
#                 x_axis = int(hub[1])
#                 y_axis = int(hub[2])
#             except ValueError as e:
#                 print(f"Not able to convert to int: {e}")
#             hub_coord: tuple[int, int] = (x_axis, y_axis)
#             if hub[3]:
#                 meta_dict: dict[str, str] = hub[3]
#             else:
#                 meta_dict = None
#             new_hub = Hub(hub_name, hub_coord, meta_dict)
#             hub_list.append(new_hub)
#         return hub_list
