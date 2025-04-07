import pygame

freeze_until = 0  # time in milliseconds

def is_frozen():
    return pygame.time.get_ticks() < freeze_until

def freeze_enemies_for(ms):
    global freeze_until
    freeze_until = pygame.time.get_ticks() + ms