import pygame
import pygame.freetype
from start_window import start
from results_window import display


def main():
    pygame.init()
    pygame.display.set_caption("IGDB Project")
    screen = pygame.display.set_mode((600, 700))

    start(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
