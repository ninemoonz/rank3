import sys
from typing import Optional


def file_opener(file_name: str) -> list[tuple[str, str, str]]:
    hub_data: tuple[str, str, str, str] = ()
    parsed_hubs: list[tuple[str, str, str]] = []
    parsed_connections: list[tuple[str, str, str]] = []
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
                    hub_data = value.strip().split(maxsplit=3)
                    parsed_hubs.append(hub_data)
                if clean_key == "connection":
                    connection_data = value.strip().replace('-', ' ').split(' ', maxsplit=2)
                    parsed_connections.append(connection_data)
    except IOError as e:
        print(e)
    return parsed_hubs, parsed_connections


if __name__ == "__main__":
    file_name = "./maps/hard/03_ultimate_challenge.txt"
    parsed_hubs, parsed_connections = file_opener(file_name)
    for hub in parsed_hubs:
        print(f"hub: {hub}")
    for cn in parsed_connections:
        print(f"connection: {cn}")
