# Level Editor for our Kroz game

# Toggle grid view
# Use mouse to place walls, items, and enemies
# Save a created level with a file name, and then play it

import pygame, sys


# Window sizes (4:3)
screen_width = 620
screen_height = 480


# Initialize Pygame and check for errors
check_errors = pygame.init()
#check_errors[1] is the second tuple of pygame.init() which contains number of errors
if check_errors[1] > 0:
    print("Error " + check_errors[1])
else:
    print("Game Successfully initialized")


# Initialize game window
pygame.display.set_caption("Kroz Level Editor")
screen = pygame.display.set_mode((screen_width, screen_height))


# Define colors using RGB values
BLACK = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
BROWN = pygame.Color(125, 50, 0)


# Function to initialize game variables
def init_vars(): 
    return {
        
    }

# Initialize game variables
game_state = init_vars()


class Object:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color
    
    def draw(self, screen):
        pass # because it will be overwritten by children classes
    
class Player(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
        # self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
    
    def draw(self, screen):
        for pos in self.position:
            pygame.draw.circle(screen, self.color, self.position, self.size)

class Wall(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
        

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Controls and Update player position
        # >= 0 to avoid negative position values
        # <= screen_height/width to prevent player from moving off the screen
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse working")
        
                
    

    # Graphics
    
    # Draw background
    screen.fill(BLACK)
    
    # Draw Player
    #player.draw(screen)
    
    # Draw Wall
    #wall_1.draw(screen)  
    
    # Update the display
    pygame.display.flip()