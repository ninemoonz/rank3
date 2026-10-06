from src import (Parser,
                 HubsFactory, ConnectionsFactory, DronesFactory,
                 Hub, MapGen)
from render_test import RenderMap


def tester(val: int):
    file_name = "./maps/medium/03_priority_puzzle.txt"
    drones, raw_hubs, raw_connections = Parser.file_opener(file_name)
    clean_drones = Parser.parse_drones(drones)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    clean_conn = Parser.parse_connections(raw_connections)
    if val == 0:
        produced_hubs = HubsFactory().make_hubs(clean_hubs, clean_drones)
        return produced_hubs
    if val == 1:
        produced_conn = ConnectionsFactory().make_connections(clean_conn)
        return produced_conn
    if val == 2:
        produced_drones = DronesFactory().make_drones(clean_drones)
        return produced_drones


if __name__ == "__main__":
    hub_list = tester(0)
    conn_list = tester(1)
    drone_list = tester(2)
    map_gen = MapGen(hub_list)
    new_map = map_gen.place_hubs()
    for y, line in enumerate(new_map):
        for x, ele in enumerate(line):
            if type(ele) is Hub:
                new_map[y][x] = "O"
            elif ele is None:
                new_map[y][x] = " "
    for line in new_map:
        print(line)
    rendered = RenderMap("priority_puzzle", hub_list)
    rendered.render_map()
