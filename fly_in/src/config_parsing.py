RawHub = tuple[str, str]
HubData = tuple[str, str, tuple[int, int], dict[str, str]]
ConnData = tuple[str, str, dict[str, str]]


class Parser:
    @staticmethod
    def file_opener(file_name: str) -> tuple[str, list[RawHub], list[str]]:
        parsed_hubs: list[RawHub] = []
        parsed_connections: list[str] = []
        drones: str = "0"
        try:
            with open(file_name) as f:
                for raw_line in f:
                    line = raw_line.strip()
                    if line == "" or line.startswith("#"):
                        continue
                    if ":" not in line:
                        raise Exception("nothing to parse")
                    key, value = line.split(":")
                    clean_key = key.strip()
                    if clean_key == "nb_drones":
                        drones = value
                    elif clean_key in ("start_hub", "hub", "end_hub"):
                        raw_data: str = value
                        parsed_hubs.append((clean_key, raw_data))
                    elif clean_key == "connection":
                        connection_data = value
                        parsed_connections.append(connection_data)
        except IOError as e:
            print(f"Cannot open file {e}")
        return drones, parsed_hubs, parsed_connections

    @staticmethod
    def parse_drones(drones: str) -> int:
        try:
            int_drones = int(drones)
            return int_drones
        except ValueError as e:
            print(e)
            return 0

    @staticmethod
    def parse_hubs(hubs_data: list[RawHub]) -> tuple[HubData, ...]:
        return_hubs: list[HubData] = []
        for hub_type, raw_data in hubs_data:
            hub_data_split = raw_data.strip().split(' ', maxsplit=3)
            if hub_data_split[0]:
                name: str = hub_data_split[0]
            if hub_data_split[1] and hub_data_split[2]:
                try:
                    coord: tuple[int, int] = (int(hub_data_split[1]),
                                              int(hub_data_split[2]))
                except ValueError as e:
                    print(e)
                    continue
            meta_list: dict[str, str] = {}
            if len(hub_data_split) > 3:
                meta_split = hub_data_split[3].strip('[]').split(' ')
                for data in meta_split:
                    key, value = data.strip().split('=')
                    meta_list[key] = value
                return_hubs.append((hub_type, name, coord, meta_list))
        return tuple(return_hubs)

    @staticmethod
    def parse_connections(connection_data: list[str]) -> tuple[ConnData, ...]:
        return_connections: list[ConnData] = []
        for raw_data in connection_data:
            split_data = (raw_data.strip().replace(' ', '-')
                          .split('-', maxsplit=2))
            hub_from: str = split_data[0]
            hub_to: str = split_data[1]
            meta_list: dict[str, str] = {}
            if len(split_data) > 2:
                meta_split = split_data[2].strip('[]').split(' ')
                for data in meta_split:
                    key, value = data.strip().split('=')
                    meta_list[key] = value
            return_connections.append((hub_from, hub_to, meta_list))
        return tuple(return_connections)
