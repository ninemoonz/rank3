RawHub = tuple[str, str, int]
RawConn = tuple[str, int]
HubData = tuple[str, str, tuple[int, int], dict[str, str], int]
ConnData = tuple[str, str, dict[str, str], int]


class ParseError(Exception):
    def __init__(self, line_no: int, msg: str) -> None:
        super().__init__(f"Line {line_no}: {msg}")
        self.line_no = line_no
        self.msg = msg


class Parser:
    @staticmethod
    def file_opener(file_name: str) -> tuple[str, list[RawHub], list[str]]:
        parsed_hubs: list[RawHub] = []
        parsed_connections: list[str] = []
        drones: int = 0
        first_line: bool = True
        try:
            with open(file_name) as f:
                for line_no, raw_line in enumerate(f, start=1):
                    line = raw_line.strip()
                    if line == "" or line.startswith("#"):
                        continue
                    if ":" not in line:
                        raise ParseError(line_no, f"missing ':' in '{line}'")
                    key, value = line.split(":", 1)
                    clean_key = key.strip()

                    if first_line:
                        if clean_key != "nb_drones":
                            raise ParseError(line_no, "first line must be "
                                             "'nb_drones: <n>'")
                        first_line = False
                        drones = value
                        drones_int = int(drones)
                        if drones_int < 0:
                            raise ParseError(line_no, "Drones cannot be "
                                             f"negative number: {drones_int}")
                    elif clean_key in ("start_hub", "hub", "end_hub"):
                        raw_data: str = value
                        parsed_hubs.append((clean_key, raw_data, line_no))
                    elif clean_key == "connection":
                        connection_data = value
                        parsed_connections.append((connection_data, line_no))
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
