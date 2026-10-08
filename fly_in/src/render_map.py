import pygame
from src import Hub, MapGen, Connection


class RenderMap:
    def __init__(self,
                 hub_list: list[Hub],
                 conn_list: list[Connection]) -> None:
        self.hub_list = hub_list
        self.conn_list = conn_list
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
        return hubs

    def coord_calibration(self,
                          margin: int,
                          cell: int,
                          coord: tuple[int, int]) -> tuple[int, int]:
        px = margin + (coord[0] - self.x_min) * cell
        py = margin + (coord[1] - self.y_min) * cell
        return px, py

    def render_map(self) -> None:
        cell: int = 200
        margin: int = 100
        width: int = 2 * margin + (self.x_max - self.x_min) * cell
        height: int = 2 * margin + (self.y_max - self.y_min) * cell
        hubs = self.extract_data()
        coord: dict[str, tuple[int, int]] = {}
        for hub in hubs:
            coord[hub[0]] = hub[1]
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(f"Fly_in")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 30)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((200, 200, 200))
            # Between this as a hidden canvas before display
            for conn in self.conn_list:
                start_pos = coord[conn.hub_from]
                end_pos = coord[conn.hub_to]
                pixel_start = self.coord_calibration(margin, cell, start_pos)
                pixel_end = self.coord_calibration(margin, cell, end_pos)
                pygame.draw.line(screen, (150, 150, 150),
                                 pixel_start, pixel_end, 30)
            for hub in hubs:
                name = hub[0]
                px, py = self.coord_calibration(margin, cell, hub[1])
                color = hub[2]
                pygame.draw.circle(screen, color, (px, py), 25)
                label = font.render(name, True, (0, 0, 0))
                screen.blit(label, (px - label.get_width() / 2, py + 30))

            # Between this as a hidden canvas before display
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
