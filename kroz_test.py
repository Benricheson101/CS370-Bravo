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
player_step = 20 # player moves 20 pixels for each step

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
        
        
        
# damage, speed, graphics, 2 states of behavior (idle and chase)
# class Enemy(Object):
    # class Enemy_fast(Enemy)
    # class Enemy_medium(Enemy)
    # class Enemy_slow(Enemy)

# class Gem(Object):
    
# class Whip(Object):
        
player = Player(game_state["player_position"], game_state["player_size"], game_state["player_color"])
        

wall_position = [screen_width // 4, screen_height // 4]
wall_size = [20,50]
wall_color = BROWN
    
wall_1 = Wall(wall_position, wall_size, wall_color)

# collide = pygame.Rect.colliderect(player, 
#                                       wall_1)


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_state["player_position"][1] - player_step >= 0:
                game_state["player_position"][1] -= player_step # moves player up by 20 pixels
            elif event.key == pygame.K_DOWN and game_state["player_position"][1] - player_step <= screen_height:
                game_state["player_position"][1] += player_step
            elif event.key == pygame.K_LEFT and game_state["player_position"][0] - player_step >= 0:
                game_state["player_position"][0] -= player_step
            elif event.key == pygame.K_RIGHT and game_state["player_position"][0] - player_step <= screen_width:
                game_state["player_position"][0] += player_step
        # if collide:
        #     print("Collision!")
                
    

    # Graphics
    
    # Draw background
    screen.fill(BLACK)
    
    # Draw Player
    player.draw(screen)
    
    # Draw Wall
    wall_1.draw(screen)  
    
    # Update the display
    pygame.display.flip()