import pygame

def draw_text(screen, text, font, color, rect):
    text_surface, _ = font.render(text, color)
    screen.blit(text_surface, rect)

def draw_button(screen, text, font, color, rect):
    pygame.draw.rect(screen, color, rect)
    draw_text(screen, text, font, (255, 255, 255), rect.topleft)

def draw_box(screen, color, rect):
    pygame.draw.rect(screen, color, rect)

def build_string_results(screen, results, font, color, rect):
    text = ''

    pos = list(rect)

    for item in results:
        draw_text(screen, f'{item.name}: rating = {item.rating:.2f}', font, color, tuple(pos))
        pos[1] += 25
    return text
