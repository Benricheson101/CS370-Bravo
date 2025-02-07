import pygame
import sys
import math

# Window sizes
screen_width = 720
screen_height = 480

# Initialize Pygame and check for errors
check_errors = pygame.init()
if check_errors[1] > 0:
    print("Error " + str(check_errors[1]))
else:
    print("Game Successfully initialized")

# Initialize game window
pygame.display.set_caption("Kroz")
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors using RGB values
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
YELLOW = pygame.Color(255, 255, 0)
BROWN = pygame.Color(125, 50, 0)

# Player properties
global player_step
player_step = 20  # player moves 20 pixels for each step

# Function to initialize game variables
def init_vars():
    return {
        "player_position": [screen_width // 2, screen_height // 2],
        "player_color": YELLOW,
        "player_size": 8,  # radius of circle
        "direction": "UP"
    }

# Initialize game variables
game_state = init_vars()

# This class will also need a score and message hint attributes
class Object:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color
    
    def draw(self, screen):
        pass  # because it will be overwritten by children classes

class Player(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.size)

class Wall(Object):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

# New Enemy class - Red Triangle that chases the player
class Enemy(Object):
    def __init__(self, position, size, color, speed, move_delay):
        super().__init__(position, size, color)
        self.speed = speed  # Speed at which the enemy chases
        self.move_delay = move_delay  # Time delay between movements in milliseconds
        self.last_move_time = pygame.time.get_ticks()  # Time of last movement
    
    def chase_player(self, player_position):
        current_time = pygame.time.get_ticks()
        
        # Check if enough time has passed for the next movement (1 second delay)
        if current_time - self.last_move_time >= self.move_delay:
            # Calculate difference in position
            dx = player_position[0] - self.position[0]
            dy = player_position[1] - self.position[1]
            
            # Prioritize moving along Y axis first, then move along X axis
            if abs(dy) > abs(dx):  # If the Y difference is greater, move vertically first
                if dy > 0:  # Move down
                    self.position[1] += self.speed
                elif dy < 0:  # Move up
                    self.position[1] -= self.speed
            else:  # If the X difference is greater or equal, move horizontally
                if dx > 0:  # Move right
                    self.position[0] += self.speed
                elif dx < 0:  # Move left
                    self.position[0] -= self.speed
            
            # Update the time of the last movement
            self.last_move_time = current_time
    
    def draw(self, screen):
        # Drawing a red triangle (enemy)
        triangle_points = [
            (self.position[0], self.position[1] - 20),  # Top point
            (self.position[0] - 20, self.position[1] + 20),  # Bottom left point
            (self.position[0] + 20, self.position[1] + 20)  # Bottom right point
        ]
        pygame.draw.polygon(screen, self.color, triangle_points)

    def check_collision(self, player_position, player_size):
        # Calculate the distance between the center of the player and the enemy
        dx = player_position[0] - self.position[0]
        dy = player_position[1] - self.position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        # Check if the distance is less than the sum of player size and enemy size
        if distance < player_size + self.size:
            return True  # Collision detected
        return False  # No collision

# Initialize player and enemy
player = Player(game_state["player_position"], game_state["player_size"], game_state["player_color"])
enemy = Enemy([100, 100], 20, RED, 20, 1000)  # Enemy moves in increments of 20 pixels with a 1-second delay

wall_position = [screen_width // 4, screen_height // 4]
wall_size = [20, 50]
wall_color = BROWN
wall_1 = Wall(wall_position, wall_size, wall_color)

# Function to display the Game Over screen
def game_over_screen():
    font = pygame.font.SysFont("Arial", 15)
    text = font.render("Game Over! Press ENTER to Restart", True, RED)
    screen.fill(BLACK)
    screen.blit(text, (screen_width // 4, screen_height // 2))
    pygame.display.flip()

# Function to restart the game
def restart_game():
    global player, enemy, game_state
    game_state = init_vars()  # Reset game variables
    player = Player(game_state["player_position"], game_state["player_size"], game_state["player_color"])  # Reset player
    enemy = Enemy([100, 100], 20, RED, 20, 1000)  # Reset enemy position

# Game loop
game_over = False
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # If game over, wait for Enter key to restart
        if game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    restart_game()
                    game_over = False
        else:
            # Controls and Update player position
            # >= 0 to avoid negative position values
            # <= screen_height/width to prevent player from moving off the screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game_state["player_position"][1] - player_step >= 0:
                    game_state["player_position"][1] -= player_step  # Moves player up by 20 pixels
                elif event.key == pygame.K_DOWN and game_state["player_position"][1] + player_step <= screen_height:
                    game_state["player_position"][1] += player_step
                elif event.key == pygame.K_LEFT and game_state["player_position"][0] - player_step >= 0:
                    game_state["player_position"][0] -= player_step
                elif event.key == pygame.K_RIGHT and game_state["player_position"][0] + player_step <= screen_width:
                    game_state["player_position"][0] += player_step

    # Move the enemy towards the player with 1-second delay
    enemy.chase_player(game_state["player_position"])

    # Check for collision between player and enemy
    if enemy.check_collision(game_state["player_position"], game_state["player_size"]):
        game_over = True  # Set game_over to True when collision happens
    
    # Graphics
    ################################################################################
    if game_over:
        game_over_screen()  # Show Game Over screen
    else:
        # Draw background
        screen.fill(BLACK)
        
        # Draw Player
        player.draw(screen)
        
        # Draw Wall
        wall_1.draw(screen)
        
        # Draw Enemy
        enemy.draw(screen)
    
    # Update the display
    pygame.display.flip()
