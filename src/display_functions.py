import pygame

# Functions that are needed to format the windows

# This function creates the text that is printed taking in a variable for font and parameters
def draw_text(screen, text, font, color, rect):
    text_surface, _ = font.render(text, color)
    screen.blit(text_surface, rect)

# This function creates each button that is needed for our program, with the text being black and in the top left
def draw_button(screen, text, font, color, rect):
    # Draw the colored rectangle
    pygame.draw.rect(screen, color, rect)
    
    # Render the text
    text_surface, _ = font.render(text, True, (255, 255, 255))  # White text
    
    # Get the dimensions of the rectangle
    x, y, width, height = rect
    
    # Calculate the position to center the text
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    
    # Blit the text onto the screen
    draw_text(screen, text, font, (255, 255, 255), text_rect.topleft)

# This function draws the box needed in the second window and takes in a different color
def draw_box(screen, color, rect):
    pygame.draw.rect(screen, color, rect)

# This function creates the string that will be printed and has a position, font and color for input
def build_string_results(screen, results, font, color, rect):
    text = ''
    # Our values are a tuple so first we need to make a list then covert it to be printed
    pos = list(rect)

    for item in results:
        draw_text(screen, f'{item.name}: rating = {item.rating:.2f}', font, color, tuple(pos))
        pos[1] += 25 # distance of 25 between each
    return text
