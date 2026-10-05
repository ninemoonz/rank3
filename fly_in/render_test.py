import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fly-in")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    # Between this as a hidden canvas before display
    pygame.draw.circle(screen, "red", (400, 300), 30, 3)
    pygame.draw.line(screen, "white", (200, 150), (700, 500), 10)
    pygame.draw.circle(screen, "blue", (700, 500), 23)
    rect = pygame.Rect(100, 100, 144, 80)
    pygame.draw.rect(screen, "grey", rect, 3)

    label = font.render("start", True, (255, 255, 255))
    label_x = 400 - label.get_width() / 2
    label_y = 300 + 30 + 6
    screen.blit(label, (label_x, label_y))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()