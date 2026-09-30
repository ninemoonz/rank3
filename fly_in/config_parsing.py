class Parser:
    def file_opener(file_name: str) -> tuple[list[str], list[str]]:
        meta_list: dict[str, str] = {}
        parsed_hubs: list[str, ...] = []
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
                    if clean_key in ("start_hub", "hub", "end_hub"):
                        hub_data: list[str] = []
                        raw_data: list[str] = value.strip().split(maxsplit=3)
                        for i in range(3):
                            hub_data.append(raw_data[i])
                        if raw_data[3]:
                            meta_split = raw_data[3].strip('[]').split(' ')
                            for data in meta_split:
                                key, value = data.strip().split('=')
                                meta_list[key] = value
                            hub_data.append(meta_list)
                            parsed_hubs.append(hub_data)
                    elif clean_key == "connection":
                        connection_data = (value
                                           .strip()
                                           .replace('-', ' ')
                                           .split(' ', maxsplit=2))
                        parsed_connections.append(connection_data)
        except IOError as e:
            print(e)
        return parsed_hubs, parsed_connections

