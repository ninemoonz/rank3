import pygame
from src import Hub, MapGen


class RenderMap:
    def __init__(self, map_name: str, hub_list: list[Hub]) -> None:
        self.map_name = map_name
        self.hub_list = hub_list
        self.x_min, self.x_max, self.y_min, self.y_max = (MapGen(hub_list)
                                                          .calc_grid())

    def extract_data(self) -> list[list[str, tuple[int, int], str]]:
        hubs: list[list[str, tuple[int, int], str]] = []
        for hub in self.hub_list:
            data: list[str, tuple[int, int], str] = []
            data.append(hub.name)
            data.append(hub.coord)
            data.append(hub.color)
            hubs.append(data)
        for one in hubs:
            print(one)
        return hubs

    def coord_calibration(self,
                          margin: int,
                          cell: int,
                          coord: tuple[int, int]) -> tuple[int, int]:
        px = margin + (coord[0] - self.x_min) * cell
        py = margin + (coord[1] - self.y_min) * cell
        return px, py

    def render_map(self) -> None:
        cell: int = 120
        margin: int = 60
        width: int = 2 * margin + (self.x_max - self.x_min) * cell
        height: int = 2 * margin + (self.y_max - self.y_min) * cell
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(f"Fly_in: {self.map_name}")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 20)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            # Between this as a hidden canvas before display
            hubs = self.extract_data()
            for hub in hubs:
                name = hub[0]
                px, py = self.coord_calibration(margin, cell, hub[1])
                color = hub[2]
                pygame.draw.circle(screen, color, (px, py), 18)
                label = font.render(name, True, (255, 255, 255))
                screen.blit(label, (px - label.get_width() / 2, py + 24))

            # Between this as a hidden canvas before display
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
