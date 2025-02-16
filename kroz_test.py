import pygame, sys
import pickle # for importing placed walls from kroz_level.py
from kroz_level import Wall  # Import Wall so unpickling works

with open("walls.pkl", "rb") as f:
    walls = pickle.load(f) # load placed wall data



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



# Function to initialize game variables
def init_vars(): 
    return {
        "player_position": [50, 125],
        "player_color": YELLOW,
        "player_size": [25, 25], # radius of circle
        "direction": "UP"
    }

# Initialize game variables
game_state = init_vars()

# this class will also need a score and message hint attributes
class Object:
    def __init__(self, position, size, color): # "position" is not an attribute of Object, just for creating Rect
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.color = color
        self.size = size # "size" was not an attribute of Object, just for creating Rect        

    def draw(self, screen):
        pass # because it will be overwritten by children classes
    
    def move(self, direction): 
        if direction == "UP":
            self.rect.y -= self.size[1] #  # moves player up by 20 pixels
        if direction == "DOWN":
            self.rect.y += self.size[1]
        if direction == "LEFT":
            self.rect.x -= self.size[0]
        if direction == "RIGHT":
            self.rect.x += self.size[0]
    
class Player(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
    
    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, self.rect)
    
    
    # def __init__(self, position, radius, color):
    #     super().__init__(position, (radius * 2, radius * 2), color) # The bounding box is radius * 2
    #     self.radius = radius
    
    # def draw(self, screen):
    #         return pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
    #         # draw.circle expects center coordinate
    
    
    

class Wall(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
    
    def draw(self, screen):
        return pygame.draw.rect(screen, self.color, self.rect)

    
# damage, speed, graphics, 2 states of behavior (idle and chase)
# class Enemy(Object):
    # class Enemy_fast(Enemy)
    # class Enemy_medium(Enemy)
    # class Enemy_slow(Enemy)

# class Gem(Object):
    
# class Whip(Object):   
        

walls = [Wall((wall.rect.x, wall.rect.y), (wall.rect.width, wall.rect.height), BROWN) for wall in walls]
# <__main__.Wall object at 0x00000268748EA960>
# print(walls)        
        
player = Player(game_state["player_position"], game_state["player_size"], game_state["player_color"])       

distances = []
for i in range(len(walls)):
    distances.append(0) # fill distances with 0 so it's not empty


# Game loop
while True:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
        elif event.type == pygame.KEYDOWN:
            # print (walls[0].rect.x, wall_2.rect.x)
            print ("Distance:", distances)
            
            
            if event.key == pygame.K_UP and [0, - game_state["player_size"][1]] not in distances: # 25
                player.move("UP") # moves player up by 20 pixels
            elif event.key == pygame.K_DOWN and [0, game_state["player_size"][1]] not in distances:
                player.move("DOWN")
            elif event.key == pygame.K_LEFT and [- game_state["player_size"][0], 0] not in distances: # 10
                player.move("LEFT")
            elif event.key == pygame.K_RIGHT and [game_state["player_size"][0], 0] not in distances:
                player.move("RIGHT")
            else:
                print("This is a wall")
            
    for i in range(len(walls)):
        distances[i] = [walls[i].rect.x - player.rect.x, walls[i].rect.y - player.rect.y] 
    
    
    
    # Collision code (this can be used for Player and Enemy)           
    # collide = pygame.Rect.colliderect(wall_1.rect, wall_2.rect)
    # if collide:
    #     print("Collision!") 
    # if event.key == pygame.K_UP and collide==False:      

    
    # Graphics
    
    # Draw background
    screen.fill(BLACK)
    
    # Draw Player
    player.draw(screen)
    
    # Draw Wall
    
    for wall in walls:
        wall.draw(screen)
        
    # Update the display
    pygame.display.flip()