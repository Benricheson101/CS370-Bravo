import pygame, sys
import pickle # for importing placed walls from kroz_level.py
from kroz_level import Wall  # Import Wall so unpickling works

with open("walls.pkl", "rb") as f:
    walls = pickle.load(f)

print(walls)

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
pygame.display.set_caption("Kroz")
screen = pygame.display.set_mode((screen_width, screen_height))


# Define colors using RGB values
BLACK = pygame.Color(0, 0, 0)
# white = pygame.Color(255, 255, 255)
# red = pygame.Color(255, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
BROWN = pygame.Color(125, 50, 0)


# Player properties
global player_step
player_step = 20 # player moves x pixels for each step

# Function to initialize game variables
def init_vars(): 
    return {
        "player_position": [screen_width // 2, screen_height // 2],
        "player_color": YELLOW,
        "player_size": 8, # radius of circle
        "direction": "UP"
    }

# Initialize game variables
game_state = init_vars()

# this class will also need a score and message hint attributes
class Object:
    def __init__(self, position, size, color): # "position" is not an attribute of Object, just for creating Rect
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.color = color        

    def draw(self, screen):
        pass # because it will be overwritten by children classes
    
class Player(Object):
    def __init__(self, position, radius, color):
        super().__init__(position, (radius * 2, radius * 2), color) # The bounding box is radius * 2
        self.radius = radius
    
    def draw(self, screen):
            return pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
            
            # draw.circle expects center coordinate
    
    def move(self, direction): 
        if direction == "UP":
            self.rect.y -= 20 #  # moves player up by 20 pixels
        if direction == "DOWN":
            self.rect.y += 20
        if direction == "LEFT":
            self.rect.x -= 8
        if direction == "RIGHT":
            self.rect.x += 8
        # print(f"Moved {direction}: New Position - {self.rect.x}, {self.rect.y}")

        
        

class Wall(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
    
    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, self.rect)
    
    def move(self, direction): 
        if direction == "UP":
            self.rect.y -= 20 #  # moves player up by 20 pixels
        if direction == "DOWN":
            self.rect.y += 20
        if direction == "LEFT":
            self.rect.x -= 8
        if direction == "RIGHT":
            self.rect.x += 8
        
        
        
# damage, speed, graphics, 2 states of behavior (idle and chase)
# class Enemy(Object):
    # class Enemy_fast(Enemy)
    # class Enemy_medium(Enemy)
    # class Enemy_slow(Enemy)

# class Gem(Object):
    
# class Whip(Object):
        
        

wall_position = [screen_width // 4, screen_height // 4]
wall_size = [8,20]
wall_color = BROWN
    
wall_1 = Wall(wall_position, wall_size, wall_color)

wall2_position = [screen_width // 8, screen_height // 8]
wall2_size = [8,20]
wall2_color = YELLOW
    
wall_2 = Wall(wall2_position, wall2_size, wall2_color)



player = Player(game_state["player_position"], game_state["player_size"], game_state["player_color"])       

wall_2_hitbox = Wall((wall2_position[0] + 2, wall2_position[1] + 2), wall2_size, wall2_color)

# Game loop
while True:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Player movement controls
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP and collide==False:
        #         player.move("UP") # moves player up by 20 pixels
        #     elif event.key == pygame.K_DOWN and collide==False:
        #         player.move("DOWN")
        #     elif event.key == pygame.K_LEFT and collide==False:
        #         player.move("LEFT")
        #     elif event.key == pygame.K_RIGHT and collide==False:
        #         player.move("RIGHT")
        
        elif event.type == pygame.KEYDOWN:
            # print (wall_1.rect.x, wall_2.rect.x)
            # print ("Distance:", distance)

            if event.key == pygame.K_UP and distance != [0, -20]:
                wall_2.move("UP") # moves player up by 20 pixels
            elif event.key == pygame.K_DOWN and distance != [0, 20]:
                wall_2.move("DOWN")
            elif event.key == pygame.K_LEFT and distance != [-8, 0]:
                wall_2.move("LEFT")
            elif event.key == pygame.K_RIGHT and distance != [8,0]:
                wall_2.move("RIGHT")
    
    
            
         
    
    distance = [wall_1.rect.x - wall_2.rect.x, wall_1.rect.y - wall_2.rect.y]    
    collide = pygame.Rect.colliderect(wall_1.rect, wall_2.rect)
    # if collide:
    #     print("Collision!")    
                
    

    # Graphics
    
    # Draw background
    screen.fill(BLACK)
    
    # Draw Player
    player.draw(screen)
    
    # Draw Wall
    wall_1.draw(screen)  
    
    wall_2.draw(screen)
        
    # Update the display
    pygame.display.flip()