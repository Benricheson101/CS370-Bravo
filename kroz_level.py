# Level Editor for our Kroz game

# Toggle grid view
# Use mouse to place walls, items, and enemies
# Save a created level with a file name, and then play it

import pygame, sys


# Window sizes (4:3)
screen_width = 640
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
WHITE = pygame.Color(255, 255, 255)
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
        
# Save level data
# def save_level():
#     return walls
        

            
# Instance of Wall class   
wall_position = [screen_width - 16, screen_height // 2 ]
wall_size = [8, 20]
wall_color = BROWN

walls = []

#wall = Wall(wall_position, wall_size, wall_color)

# player = Player((screen_width // 2, screen_height // 2), 6, YELLOW)

def nearest_factor_x(xCoord):
    if xCoord % 8 != 0:
        xCoord = xCoord - 1
    return xCoord

def nearest_factor_y(yCoord):
    if yCoord % 20 != 0:
        yCoord = yCoord - 1
    return yCoord

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # save_level()
            pygame.quit()
            sys.exit()
            
        # Controls and Update player position
        # >= 0 to avoid negative position values
        # <= screen_height/width to prevent player from moving off the screen
        x, y = pygame.mouse.get_pos()
        wall_cursor = Wall((x - 8, y - 20), wall_size, wall_color) # -8, -20 so mouse isn't in the way
        
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            wall_placed = Wall((nearest_factor_x(x) - 8, nearest_factor_y(y) - 20), wall_size, wall_color)
            walls.append(wall_placed)
            print(f' Left Mouse clicked at {x}, {y}')
            print(f'Wall placed at {nearest_factor_x(x) - 8}, {nearest_factor_y(y) - 20}')
           
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()
            if len(walls) != 0:
                walls.pop(-1)
            
            # print(f' Right Mouse clicked at {x}, {y}')
        
                
    

    # Graphics
    
    # Draw background
    screen.fill(BLACK)
    
    # Draw Player
    # player.draw(screen)
    
    # Draw Wall
    
    wall_cursor.draw(screen)
    
    for wall in range(len(walls)):
        walls[wall].draw(screen)
        # print(walls)
    
    # Draw Grid
    def draw_grid():
        grid_x = 0
        grid_y = 0
        for y in range (screen_height // wall_size[1]):
            for x in range (screen_width // wall_size[0]):
                 # pygame.Rect(coordinates (x,y), size (width, height), border thickness)
                pygame.draw.rect(screen, WHITE, pygame.Rect((grid_x, grid_y), (8, 20)), 1)
                grid_x += 8
            grid_x = 0
            grid_y += 20
        
            
            
           
                
                
                
                
            
        # for x in range (screen_height // wall_size[1]):
        #     # pygame.Rect(coordinates (x,y), size (width, height), border style)
        #     pygame.draw.rect(screen, WHITE, pygame.Rect((0, grid_y), (8, 20)), 1)
        #     grid_y += 20
        # for y in range (screen_width // wall_size[0]):
        #     pygame.draw.rect(screen, WHITE, pygame.Rect((grid_x, 0), (8, 20)), 1)
        #     grid_x += 8
            
    draw_grid()
    
    
            
    
    # Update the display
    pygame.display.flip()

