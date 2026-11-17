from src.config_parsing import ParseError, HubData


class Validator:
    def __init__(self, parsed_hubs: tuple[HubData, ...]) -> None:
        self.parsed_hubs = parsed_hubs

    def is_unique(self) -> None:
        hub_names: list[str] = []
        for hub in self.parsed_hubs:
            hub_names.append(hub[1])
            if not len(hub_names) == len(set(hub_names)):
                raise ParseError(hub[-1], "Duplicated name "
                                 f"detected '{hub[1]}'")

    def unique_zone(self) -> None:
        start_count: int = 0
        end_count: int = 0
        for zone in self.parsed_hubs:
            if zone[0] == "start_hub":
                start_count += 1
                if start_count > 1:
                    raise ParseError(zone[-1], "More than one "
                                     "zone type 'start_hub' detected.")
            elif zone[0] == "end_hub":
                end_count += 1
                if end_count > 1:
                    raise ParseError(zone[-1], "More than one "
                                     "zone type 'end_hub' detected.")
        if start_count == 0:
            raise ParseError(0, "No 'start_hub' found. "
                             "Check config file")
        if end_count == 0:
            raise ParseError(0, "No 'end_hub' found. "
                             "Check config file")
