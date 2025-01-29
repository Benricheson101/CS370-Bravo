
# https://www.pygame.org/docs/ref/mouse.html

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
gameScreen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Mouse Click - Test Game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # Left click
                print('Left mouse button pressed!')
            elif pygame.mouse.get_pressed()[2]: # Right click
                print('Right mouse button pressed!')
                
            # For coordinates:
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     x, y = pygame.mouse.get_pos()
            #     print(f'Mouse clicked at {x}, {y}')

pygame.quit()