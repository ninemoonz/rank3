
from src import Hub

class MapGen:
	def calc_grid(hub_list: list[Hub]) -> tuple[int, int]:
		coord_list: list[tuple[int, int]] = ()
		for hub in hub_list:
			print(hub.coord)


if __name__ == "__main__":
	new_map = MapGen.calc_grid()