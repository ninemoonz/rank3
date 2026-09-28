from pydantic import BaseModel, Field, model_validator
from typing import Optional


class Hub(BaseModel):
    hub_name: str = Field(min_length=1)
    x_axis: str
    y_axis: str
    metadata: Optional[list[str]] = None


class HubsFactory:
    def make_hub(self, hub_info: list[str]) -> list[Hub]:
        new_hub = Hub()
        hub_list: list[Hub] = []
        for hub in hub_info:
            new_hub.hub_name = hub[0]
            new_hub.x_axis = hub[1]
            new_hub.y_axis = hub[2]
            if hub[3]:
                new_hub.metadata = hub[3]
            else:
                new_hub.metadata = None
            hub_list.append(new_hub)
        return hub_list
