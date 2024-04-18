import pygame
import pygame.freetype

background = pygame.image.load('Designer.png')
def draw_text(screen, text, font, color, rect):
    text_surface, _ = font.render(text, color)
    screen.blit(text_surface, rect)

def main():
    pygame.init()
    pygame.display.set_caption("IGDB Project")
    screen = pygame.display.set_mode((600, 700))
    font = pygame.freetype.SysFont(None, 24)

    clock = pygame.time.Clock()
    input_box = pygame.Rect(00, 50, 300, 100)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, color, input_box, 2)
        draw_text(screen, text, font, (255, 255, 255), input_box.topleft)
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
