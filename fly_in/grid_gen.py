from src import Hub


class MapGen:
    def __init__(self, hub_list: list[Hub]) -> None:
        self.hubs = hub_list
        self.x_min, self.x_max, self.y_min, self.y_max = self.calc_grid()
        self.grid = self.make_grid()

    def calc_grid(self) -> tuple[int, int, int, int]:
        x_list: list[int] = []
        y_list: list[int] = []
        for hub in self.hubs:
            x_list.append(hub.coord[0])
            y_list.append(hub.coord[1])
        x_min = min(x_list)
        x_max = max(x_list)
        y_min = min(y_list)
        y_max = max(y_list)
        return x_min, x_max, y_min, y_max

    def make_grid(self) -> list[list[tuple[int, int]]]:
        grid: list[list[int]] = []
        for y in range(self.y_min, self.y_max + 1):
            row_list: list[int] = []
            for x in range(self.x_min, self.x_max + 1):
                grid_coord: tuple[int, int] = x, y
                row_list.append(grid_coord)
            grid.append(row_list)
        return grid

    def place_hubs(self):
        new_grid = self.grid
        for y, line in enumerate(new_grid):
            for x, coord in enumerate(line):
                for hub in self.hubs:
                    if hub.coord == coord:
                        new_grid[y][x] = hub
        for y, line in enumerate(new_grid):
            for x, element in enumerate(line):
                if type(element) is not Hub:
                    new_grid[y][x] = None
        return new_grid
