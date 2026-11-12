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
    def file_opener(file_name: str) -> tuple[tuple[str, int],
                                             list[RawHub],
                                             list[RawConn]]:
        parsed_hubs: list[RawHub] = []
        parsed_connections: list[RawConn] = []
        parsed_drones: tuple[str, int] = ("", 0)
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
                        parsed_drones = value, line_no
                    elif clean_key == "nb_drones":
                        raise ParseError(line_no, "nb_drones defined twice")
                    elif clean_key in ("start_hub", "hub", "end_hub"):
                        raw_data: str = value
                        parsed_hubs.append((clean_key, raw_data, line_no))
                    elif clean_key == "connection":
                        connection_data = value
                        parsed_connections.append((connection_data, line_no))
                    else:
                        raise ParseError(line_no, f"unknown key '{clean_key}'")
            if first_line:
                raise ParseError(0, "File is empty")
        except IOError as e:
            raise ParseError(0, f"Cannot open file: {e}")
        return parsed_drones, parsed_hubs, parsed_connections

    @staticmethod
    def parse_drones(drones: str, line_no: int) -> int:
        try:
            int_drones = int(drones)
        except ValueError:
            raise ParseError(line_no, "nb_drones must be an int: "
                             f"'{drones.strip()}'")
        if int_drones <= 0:
            raise ParseError(line_no, "Drones cannot be "
                             f"negative or zero: {int_drones}")
        return int_drones

    @staticmethod
    def parse_hubs(hubs_data: list[RawHub]) -> tuple[HubData, ...]:
        return_hubs: list[HubData] = []
        for hub_type, raw_data, line_no in hubs_data:
            hub_data_split = raw_data.split(maxsplit=3)
            if len(hub_data_split) < 3:
                raise ParseError(line_no, "Expected '<name> <x> <y> "
                                 "[metadata]'")
            name: str = hub_data_split[0]
            try:
                coord: tuple[int, int] = (int(hub_data_split[1]),
                                          int(hub_data_split[2]))
            except ValueError:
                raise ParseError(line_no, "Coordinate must be integers: "
                                 f"{hub_data_split[1]} "
                                 f"{hub_data_split[2]}") 

            meta_list: dict[str, str] = {}
            if len(hub_data_split) > 3:
                meta = hub_data_split[3]
                if not (meta.startswith('[') and meta.endswith(']')):
                    raise ParseError(line_no, f"Invalid metadata: {meta}")
                for tag in meta[1:-1].split():
                    if tag.count('=') != 1:
                        raise ParseError(line_no, f"Invalid tag: '{tag}'")
                    key, value = tag.split('=')
                    if key not in ("zone", "color", "max_drones"):
                        raise ParseError(line_no, f"unknown metadata: '{key}'")
                    if key == "max_drones":
                        if not value.isdigit():
                            raise ParseError(line_no, "Must be digits: "
                                             f"current value: {value}")
                        if int(value) <= 0:
                            raise ParseError(line_no, "Need positive integer, "
                                             f"Current value: {value}")
                    if (key == "zone" and value not in ("normal",
                                                        "restricted",
                                                        "priority",
                                                        "blocked")):
                        raise ParseError(line_no, "zone types: 'normal', "
                                         "'restricted', 'priority', 'blocked'"
                                         f" current type: '{value}'")
                    meta_list[key] = value
            return_hubs.append((hub_type, name, coord, meta_list, line_no))
        return tuple(return_hubs)

    @staticmethod
    def parse_connections(
        connection_data: list[RawConn], hub_names: set[str]
                        ) -> tuple[ConnData, ...]:
        return_connections: list[ConnData] = []
        link_history: set[frozenset[str]] = set()
        for raw_data, line_no in connection_data:
            parts = raw_data.split(maxsplit=1)
            if len(parts) == 0:
                raise ParseError(line_no, "empty connection")
            names = parts[0].split('-')
            if len(names) != 2 or names[0] == "" or names[1] == "":
                raise ParseError(line_no, "Connection must be "
                                 f"'<name1>-<name2>': '{parts[0]}'")
            hub_a, hub_b = names
            pair = frozenset((hub_a, hub_b))
            if pair in link_history:
                raise ParseError(line_no, "duplicate connection")
            link_history.add(pair)

            if hub_a not in hub_names:
                raise ParseError(line_no, f"hub does not exist: '{hub_a}'")
            if hub_b not in hub_names:
                raise ParseError(line_no, f"hub does not exist: '{hub_b}'")
            if hub_a == hub_b:
                raise ParseError(line_no, "should not connect same hub: "
                                 f"'{hub_a}'-'{hub_b}'")
            meta_list: dict[str, str] = {}
            if len(parts) == 2:
                meta_data = parts[1]
                if not (meta_data.startswith('[') and meta_data.endswith(']')):
                    raise ParseError(line_no, f"invalid metadata: {meta_data}")
                for tag in meta_data[1:-1].split():
                    if tag.count('=') != 1:
                        raise ParseError(line_no, f"invalid tag: '{tag}'")
                    max_cap, count = tag.split('=')
                    if max_cap != "max_link_capacity":
                        raise ParseError(line_no, "metadata should be "
                                         f"'max_link_capacity': {max_cap}")
                    if not count.isdigit():
                        raise ParseError(line_no, "value should be "
                                         f"a number: {count}")
                    if int(count) <= 0:
                        raise ParseError(line_no, "value should "
                                         f"be greater than 0: {count}")
                    meta_list[max_cap] = count
            return_connections.append((hub_a, hub_b, meta_list, line_no))
        return tuple(return_connections)
