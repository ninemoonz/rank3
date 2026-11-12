import sys
from pydantic import ValidationError
from graph_gen import Graph
from new_dijkstra import Dijkstra
from typing import TYPE_CHECKING
from src.config_parsing import ParseError, HubData, ConnData
from src import (Parser,
                 HubsFactory,
                 ConnectionsFactory,
                 DronesFactory,
                 RenderMap)
from validation import Validator


if TYPE_CHECKING:
    from src import Drone, Hub, Connection


def parse_all(file_name: str) -> tuple[int,
                                       tuple[HubData, ...],
                                       tuple[ConnData, ...]]:
    drones, raw_hubs, raw_conn = Parser.file_opener(file_name)
    clean_drones = Parser.parse_drones(drones[0], drones[1])
    clean_hubs = Parser.parse_hubs(raw_hubs)
    hub_names: set[str] = set()
    for hub in clean_hubs:
        hub_names.add(hub[1])
    clean_conn = Parser.parse_connections(raw_conn, hub_names)
    return clean_drones, clean_hubs, clean_conn


def run_factory(
        parsed_drones: int,
        parsed_hubs: tuple[HubData, ...],
        parsed_conns: tuple[ConnData, ...]
        ) -> tuple[list["Drone"], list["Hub"], list["Connection"]]:
    produced_drones = DronesFactory().make_drones(parsed_drones)
    produced_hubs = HubsFactory().make_hubs(parsed_hubs, parsed_drones)
    produced_conn = ConnectionsFactory().make_connections(parsed_conns)
    return produced_drones, produced_hubs, produced_conn


def validation(parsed_hub: tuple[HubData, ...]) -> None:
    hubs_validator = Validator(parsed_hub)
    hubs_validator.is_unique()
    hubs_validator.unique_zone()


if __name__ == "__main__":
    file_name = "./maps/test/00_test_map.txt"
    try:
        parsed_drone, parsed_hub, parsed_conn = parse_all(file_name)
        validation(parsed_hub)
        drones_list, hubs_list, conns_list = run_factory(parsed_drone,
                                                         parsed_hub,
                                                         parsed_conn)
    except (ParseError, ValidationError) as e:
        print(f"[Error] {e}", file=sys.stderr)
        sys.exit(1)

    # new_graph = Graph(hubs_list, conns_list)
    # D = Dijkstra(new_graph)
    # shortest = D.shortest_distances()
    # print(f"shortest path: {shortest}")
    # display_map = RenderMap(hubs_list, conns_list)
    # display_map.render_map()
