from pydantic import BaseModel, Field, model_validator
from typing import Optional


class Drone(BaseModel):
    drone_nb: int
    before_hub: Optional[tuple[str, tuple[int, int]]] = Field(default=None)
    present_hub: tuple[str, tuple[int, int]] | None = Field(default=None)
    next_hub: Optional[tuple[str, tuple[int, int]]] = Field(default=None)

    def describe(self) -> None:
        print("[Drones Description]")
        print(f"- drone number: {self.drone_nb}")
        print(f"- Past Hub: {self.before_hub}")
        print(f"- Current Hub: {self.present_hub}")
        print(f"- Next Hub: {self.next_hub}\n")


class Hub(BaseModel):
    hub_type: str = Field(min_length=1)
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
        if self.zone not in ("normal", "blocked", "restricted", "priority"):
            raise ValueError("zone type should be one of four: "
                             "'normal', 'blocked', 'restricted', 'priority'")
        return self

    def describe(self) -> None:
        print("[Description]")
        print(f"- hub type: {self.hub_type}")
        print(f"- hub name: {self.name}")
        print(f"- coordinate: {self.coord}")
        print(f"[metadata]\n"
              f"- zone: {self.zone}\n"
              f"- color: {self.color}\n"
              f"- max drones: {self.max_drones}\n")


class Connection(BaseModel):
    hub_from: str
    hub_to: str
    max_link_capacity: int = Field(default=1)

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
        print(f"- Connection from: {self.hub_from}")
        print(f"- Connection to: {self.hub_to}")
        print(f"- Max link capacity: {self.max_link_capacity}\n")
