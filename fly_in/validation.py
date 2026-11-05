from src.config_parsing import ParseError


class Validator:
    def __init__(self, parsed_hubs: list[str]) -> None:
        self.parsed_hubs = parsed_hubs

    def is_unique(self) -> bool:
        hub_names: list[str] = []
        for hub in self.parsed_hubs:
            print(f"hub: {hub}")
            hub_names.append(hub[1])
        if not len(hub_names) == len(set(hub_names)):
            raise ParseError(hub[-1], "Duplicated name detected")

    def unique_zone(self) -> bool:
        zone_type: list[str] = []
        for zone in self.parsed_hubs:
            print(f"zone: {zone}")
            zone_type.append(zone[0])
        print(zone_type)
        if (not zone_type.count("start_hub") == 1 or
           "start_hub" not in zone_type):
            raise ParseError(zone[-1], "There are more than one 'start_hub'"
                             " or none. Pleaes check config file.")
        if (not zone_type.count("end_hub") == 1 or
           "end_hub" not in zone_type):
            raise ParseError(zone[-1], "There are more than one 'end_hub'"
                             " or none. Pleaes check config file.")
