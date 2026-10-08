from graph_gen import Graph
from typing import TYPE_CHECKING
from src import (Parser,
                 HubsFactory,
                 ConnectionsFactory,
                 DronesFactory,
                 RenderMap)

if TYPE_CHECKING:
    from src import Drone, Hub, Connection


def parse_all(file_name: str) -> tuple[int, list[str], list[str]]:
    drones, raw_hubs, raw_conn = Parser.file_opener(file_name)
    clean_drones = Parser.parse_drones(drones)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    clean_conn = Parser.parse_connections(raw_conn)
    return clean_drones, clean_hubs, clean_conn


def make_instance(parsed_drones: str,
                  parsed_hubs: list[str],
                  parsed_conns: list[str]) -> tuple[list["Drone"],
                                                    list["Hub"],
                                                    list["Connection"]]:
    produced_drones = DronesFactory().make_drones(parsed_drones)
    produced_hubs = HubsFactory().make_hubs(parsed_hubs, parsed_drones)
    produced_conn = ConnectionsFactory().make_connections(parsed_conns)
    return produced_drones, produced_hubs, produced_conn


if __name__ == "__main__":
    file_name = "./maps/hard/01_maze_nightmare.txt"
    parsed_drone, parsed_hub, parsed_conn = parse_all(file_name)
    drones_list, hubs_list, conns_list = make_instance(parsed_drone,
                                                       parsed_hub,
                                                       parsed_conn)
    new_graph = Graph(hubs_list, conns_list)
    for name in new_graph.link_to:
        print(name, "->", [next_name for next_name, conns in new_graph.link_to[name]])
    display_map = RenderMap(hubs_list, conns_list)
    display_map.render_map()
