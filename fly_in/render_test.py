import pygame
from src import Hub, MapGen


class RenderMap:
    def __init__(self, map_name: str, hub_list: list[Hub]) -> None:
        self.map_name = map_name
        self.hub_list = hub_list
        self.x_min, self.x_max, self.y_min, self.y_max = (MapGen(hub_list)
                                                          .calc_grid())

    def coord_calibration(self, margin: int, cell: int):
        for hub in self.hub_list:
            x, y = hub.coord
            px = margin + (x - self.x_min) * cell
            py = margin + (y - self.y_min) * cell

    def render_map(self) -> None:
        pygame.init()
        cell: int = 120
        margin: int = 120
        width: int = 2 * margin + (self.x_max - self.x_min) * cell
        height: int = 2 * margin + (self.y_max - self.y_min) * cell
        if self.x_min < 0:
            ...
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.map_name)
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 20)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            # Between this as a hidden canvas before display
            pygame.draw.circle(screen, (0, 255, 0), (width / 2,
                                                     height / 2), 10, 3)

            # rect = pygame.Rect(100, 100, 144, 80)
            # pygame.draw.rect(screen, "grey", rect, 3)
            label = font.render("start", True, (0, 255, 0))
            label_width = label.get_width()
            label_x = (width / 2) - (label_width / 2)
            label_y = (height / 2) + 10 + 10
            screen.blit(label, (label_x, label_y))

            # Between this as a hidden canvas before display
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
