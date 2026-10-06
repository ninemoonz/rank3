import pygame


pygame.init()
width: int = 800
height: int = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fly-in")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)
running = True
x: int = 0
y: int = 0
while y <= height or x <= width:
    y += 50
    x += 50
    pygame.draw.line(screen, "white", (0, y), (800, y), 2)
    pygame.draw.line(screen, "white", (x, 0), (x, 600), 2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill((0, 0, 0))
    # Between this as a hidden canvas before display
    # pygame.draw.circle(screen, "red", (400, 300), 30, 3)
    # rect = pygame.Rect(100, 100, 144, 80)
    # pygame.draw.rect(screen, "grey", rect, 3)
    # label = font.render("start", True, (255, 255, 255))
    # label_x = 400 - label.get_width() / 2
    # label_y = 300 + 30 + 6
    # screen.blit(label, (label_x, label_y))

    # Between this as a hidden canvas before display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()