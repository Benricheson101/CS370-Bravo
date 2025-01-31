import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Two Shapes for One Object")

# Define a class for the object
class MyObject:
    def __init__(self, rect_pos, rect_size, circle_pos, circle_radius):
        self.rect_pos = rect_pos
        self.rect_size = rect_size
        self.circle_pos = circle_pos
        self.circle_radius = circle_radius

    def draw(self, surface):
        # Draw the rectangle
        pygame.draw.rect(surface, (255, 0, 0), (*self.rect_pos, *self.rect_size))
        # Draw the circle
        pygame.draw.circle(surface, (0, 0, 255), self.circle_pos, self.circle_radius)

# Create an instance of MyObject
my_object = MyObject((100, 100), (200, 100), (200, 150), 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the object
    my_object.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
