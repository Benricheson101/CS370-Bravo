# Level Editor for our Kroz game

# Toggle grid view
# Use mouse to place walls, items, and enemies
# Save a created level with a file name, and then play it

import pygame, sys
import pickle


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
# 2:5
wall_size = [10, 25]
wall_color = BROWN

walls = []


# Function for saving placed walls
def save_walls():
    with open("walls.pkl", "wb") as f:
        pickle.dump(walls, f)
    

# Game loop
if __name__ == "__main__":
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_walls()
                pygame.quit()
                sys.exit()
                
    
            x, y = pygame.mouse.get_pos()
            
            
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                wall_placed = Wall((grid_placed.topleft[0], grid_placed.topleft[1]), wall_size, wall_color)
                walls.append(wall_placed)
                print(wall_placed)
                # print(f' Left Mouse clicked at {x}, {y}')
                print(f'Wall placed at {grid_placed.topleft[0]}, {grid_placed.topleft[1]}')
            
            # If rmb pressed and there's nothing placed, nothing will happen
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
        
        
        
        for wall in range(len(walls)):
            walls[wall].draw(screen)
            # print(walls)
        
        # Draw Grid
        # def draw_grid():
        grid_x = 0
        grid_y = 0
        grids = []
        for y in range (screen_height // wall_size[1]):
            for x in range (screen_width // wall_size[0]):
                    # pygame.Rect(coordinates (x,y), size (width, height), border thickness)
                grid = pygame.draw.rect(screen, WHITE, pygame.Rect((grid_x, grid_y), 
                                                                   (wall_size[0], wall_size[1])), 1)
                if grid.collidepoint(pygame.mouse.get_pos()):
                    grid_placed = pygame.draw.rect(screen, YELLOW, pygame.Rect((grid_x, grid_y), 
                                                                               (wall_size[0], wall_size[1])))
                    
                    
                # print(grid)
                grid_x += wall_size[0]
            grid_x = 0
            grid_y += wall_size[1]
            # grids.append(grid)    
        # draw_grid()
        
        
                
        
        # Update the display
        pygame.display.flip()

    