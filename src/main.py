import pygame

# THANK YOU!
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("IGDB Project")
    screen = pygame.display.set_mode((600, 700))
    screen.fill((0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


