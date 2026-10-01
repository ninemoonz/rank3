class Parser:
    def file_opener(file_name: str) -> tuple[str, list[str], list[str]]:
        parsed_hubs: list[str] = []
        parsed_connections: list[tuple[str, ...]] = []
        try:
            with open(file_name, "r") as f:
                for raw_line in f:
                    line = raw_line.strip()
                    if line == "" or line.startswith("#"):
                        continue
                    if ":" not in line:
                        raise Exception("nothing to parse")
                    key, value = line.split(":")
                    clean_key = key.strip()
                    if clean_key == "nb_drones":
                        try:
                            drones: str = value
                        except ValueError as e:
                            print(e)
                    elif clean_key in ("start_hub", "hub", "end_hub"):
                        raw_data: str = value
                        parsed_hubs.append((clean_key, raw_data))
                    elif clean_key == "connection":
                        connection_data = value
                        parsed_connections.append(connection_data)
        except IOError as e:
            print(f"Cannot open file {e}")
        return drones, parsed_hubs, parsed_connections

    def parse_drones(drones: str) -> int:
        try:
            int_drones = int(drones)
        except ValueError as e:
            print(e)
        return int_drones

    def parse_hubs(hubs_data: list[str]) -> tuple[str, ...]:
        return_hubs: list[str] = []
        for hub_type, raw_data in hubs_data:
            polished: list[str] = [hub_type]
            hub_data_split = raw_data.strip().split(' ', maxsplit=3)
            if hub_data_split[0]:
                polished.append(hub_data_split[0])
            if hub_data_split[1] and hub_data_split[2]:
                try:
                    coord: tuple[int, int] = (int(hub_data_split[1]),
                                              int(hub_data_split[2]))
                    polished.append(coord)
                except ValueError as e:
                    print(e)
            if len(hub_data_split) > 3:
                meta_list: list[dict[str, str]] = {}
                meta_split = hub_data_split[3].strip('[]').split(' ')
                for data in meta_split:
                    key, value = data.strip().split('=')
                    meta_list[key] = value
                polished.append(meta_list)
                return_hubs.append(polished)
            else:
                continue
        return tuple(return_hubs)

    def parse_connections(connection_data: list[str]) -> tuple[str, ...]:
        return_connections: list[str] = []
        for raw_data in connection_data:
            split_data = (raw_data.strip().replace(' ', '-')
                          .split('-', maxsplit=2))
            polish_data: list[str] = []
            if split_data[0]:
                polish_data.append(split_data[0])
            if split_data[1]:
                polish_data.append(split_data[1])
            if len(split_data) > 2:
                meta_list: list[dict[str, str]] = {}
                meta_split = split_data[2].strip('[]').split(' ')
                for data in meta_split:
                    key, value = data.strip().split('=')
                    meta_list[key] = value
                polish_data.append(meta_list)
            return_connections.append(polish_data)
        return tuple(return_connections)
