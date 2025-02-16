import pygame, sys

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

  
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()