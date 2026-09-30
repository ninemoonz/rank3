from typing import TextIO


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
                        parsed_hubs.append(raw_data)
                    elif clean_key == "connection":
                        connection_data = value
                        parsed_connections.append(connection_data)
        except IOError as e:
            print(e)
        return drones, parsed_hubs, parsed_connections

    def parse_drones(drones: str) -> int:
        try:
            int_drones = int(drones)
        except ValueError as e:
            print(e)
        return int_drones

    def parse_hubs(hubs_data: list[str]) -> tuple[str, ...]:
        return_hubs = []
        for raw_data in hubs_data:
            polished: list[str] = []
            hub_data_split = raw_data.strip().split(' ', maxsplit=3)
            if hub_data_split[0]:
                polished.append(hub_data_split[0])
            if hub_data_split[1] and hub_data_split[2]:
                try:
                    coord: tuple[int, int] = (int(hub_data_split[1]), int(hub_data_split[2]))
                    polished.append(coord)
                except ValueError as e:
                    print(e)
            if hub_data_split[3]:
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

    def parse_connections(connection_data: list[str]) -> list[str]:
        print(connection_data)

    # def file_opener(file_name: str) -> tuple[int, list[str], list[str]]:
    #     meta_list: dict[str, str] = {}
    #     parsed_hubs: list[str] = []
    #     parsed_connections: list[tuple[str, ...]] = []
    #     try:
    #         with open(file_name, "r") as f:
    #             for raw_line in f:
    #                 line = raw_line.strip()
    #                 if line == "" or line.startswith("#"):
    #                     continue
    #                 if ":" not in line:
    #                     raise Exception("nothing to parse")
    #                 key, value = line.split(":")
    #                 clean_key = key.strip()
    #                 if clean_key in ("start_hub", "hub", "end_hub"):
    #                     hub_data: list[str] = []
    #                     raw_data: list[str] = value.strip().split(maxsplit=3)
    #                     for i in range(3):
    #                         hub_data.append(raw_data[i])
    #                     if raw_data[3]:
    #                         meta_split = raw_data[3].strip('[]').split(' ')
    #                         for data in meta_split:
    #                             key, value = data.strip().split('=')
    #                             meta_list[key] = value
    #                         hub_data.append(meta_list)
    #                     else:
    #                         continue
    #                     parsed_hubs.append(hub_data)
    #                 elif clean_key == "nb_drones":
    #                     try:
    #                         nb_drones: int = int(value)
    #                     except ValueError as e:
    #                         print(e)
    #                 elif clean_key == "connection":
    #                     connection_data = (value
    #                                        .strip()
    #                                        .replace('-', ' ')
    #                                        .split(' ', maxsplit=2))
    #                     parsed_connections.append(connection_data)
    #     except IOError as e:
    #         print(e)
    #     return nb_drones, parsed_hubs, parsed_connections
