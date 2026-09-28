from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Optional


class Zone(BaseModel):
    drones: int = Field(gt=0)
    hubs: list[str, tuple[int, int], Optional[str]]
    connections: list[tuple[str, str, Optional[str]]]


class Hub(BaseModel):
    def __init__(self, hub_name: str,
                 x_axis: int, y_axis: int, metadata: Optional[str]) -> None:
        self.hub_name: str = hub_name
        self.x_axis: int = x_axis Field(ge=0)
        self.y_axis: int = Field(ge=0)
        metadata: Optional[list[str]]

    @model_validator(mode='after')
    def hubs_check(self) -> None:
        ...
        return self


class HubsFactory():
    def __init__(self, hubs: list[Hub]) -> Hub:
        ...
