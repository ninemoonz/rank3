from src import Parser, HubsFactory, ConnectionsFactory, DronesFactory, Hub


class MapGen:
    def calc_grid(hub_list: list[Hub]) -> tuple[int, int]:
        x_list: list[int] = []
        y_list: list[int] = []
        for hub in hub_list:
            x_list.append(hub.coord[0])
            y_list.append(hub.coord[1])
        x_min = min(x_list)
        x_max = max(x_list)
        y_min = min(y_list)
        y_max = max(y_list)
        x_len = x_max - x_min
        y_len = y_max - y_min
        return x_len, y_len


    def make_grid(grid_info) -> list[list[int]]:
        grid: list[list[int]] = []
        for _ in range(grid_info[1] + 1):
            row_list: list[int] = []
            for i in range(grid_info[0] + 1):
                row_list.append(i)
            grid.append(row_list)
        return grid


def tester(val: int) -> None:
    file_name = "./maps/hard/01_maze_nightmare.txt"
    drones, raw_hubs, raw_connections = Parser.file_opener(file_name)
    clean_drones = Parser.parse_drones(drones)
    clean_hubs = Parser.parse_hubs(raw_hubs)
    clean_conn = Parser.parse_connections(raw_connections)
    if val == 0:
        hubs_list: list[Hub] = []
        print("\n===Produce hubs in factory===\n")
        produced_hubs = HubsFactory().make_hubs(clean_hubs, clean_drones)
        for ahub in produced_hubs:
            ahub.describe()
            hubs_list.append(ahub)
        return hubs_list
        
    if val == 1:
        print("\n===Produce Connection in factory===\n")
        produced_conn = ConnectionsFactory().make_connections(clean_conn)
        for conn in produced_conn:
            conn.describe()
    if val == 2:
        print("\n===Produce Drone in factory===\n")
        produced_drones = DronesFactory().make_drones(clean_drones)
        for adrone in produced_drones:
            adrone.describe()


if __name__ == "__main__":
    hub_list = tester(0)
    max_coord = MapGen.calc_grid(hub_list)
    print(max_coord)
    grid = MapGen.make_grid(max_coord)
    for line in grid:
        print(line)
