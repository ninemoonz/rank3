class Hub():
    def __init__(self,
                 name: str,
                 coord: tuple[int, int],
                 metadata: dict[str, int] | None) -> None:
        self.name = name
        self.coord = coord
        self.metadata = metadata

    def describe(self) -> None:
        print(f"hub name: {self.name}")
        print(f"coordinate: {self.coord}")
        print(f"metadata: {self.metadata}")


class HubsFactory:
    def make_hub(self, hub_info: list[str]) -> list[Hub]:
        hub_coord: tuple[int, int] = ()
        hub_list: list[Hub] = []
        for hub in hub_info:
            hub_name: str = hub[0]
            try:
                x_axis = int(hub[1])
                y_axis = int(hub[2])
            except ValueError as e:
                print(f"Not able to convert to int: {e}")
            hub_coord = (x_axis, y_axis)
            if hub[3]:
                metadata = hub[3]
            else:
                metadata = None
            new_hub = Hub(hub_name, hub_coord, metadata)
            hub_list.append(new_hub)
        return hub_list
