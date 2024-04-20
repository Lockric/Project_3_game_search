import pygame

def draw_text(screen, text, font, color, rect):
    text_surface, _ = font.render(text, color)
    screen.blit(text_surface, rect)

def draw_button(screen, text, font, color, rect):
    pygame.draw.rect(screen, color, rect)
    draw_text(screen, text, font, (255, 255, 255), rect.topleft)

def draw_box(screen, color, rect):
    pygame.draw.rect(screen, color, rect)
    