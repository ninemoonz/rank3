from src.config_parsing import ParseError


class Validator:
    def __init__(self, parsed_hubs: list[str]) -> None:
        self.parsed_hubs = parsed_hubs

    def is_unique(self) -> None:
        hub_names: list[str] = []
        for hub in self.parsed_hubs:
            hub_names.append(hub[1])
            if not len(hub_names) == len(set(hub_names)):
                raise ParseError(hub[-1], f"Duplicated name detected '{hub[1]}'")

    def unique_zone(self) -> None:
        zone_type: list[str] = []
        for zone in self.parsed_hubs:
            print(f"zone: {zone[0]}")
            zone_type.append(zone[0])
        if (not zone_type.count("start_hub") == 1 or
           "start_hub" not in zone_type):
            raise ParseError(zone[-1], "There are more than one 'start_hub'"
                             " or none. Pleaes check config file.")
        elif (not zone_type.count("end_hub") == 1 or
              "end_hub" not in zone_type):
            raise ParseError(zone[-1], "There are more than one 'end_hub'"
                             " or none. Pleaes check config file.")
        print(f"zone type: {zone_type}")
