import pygame, sys


# Window sizes
screen_width = 720
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


# Circle properties
circle_radius = 8 # size of player object
player_step = 20 # player moves 20 pixels for each step

# Function to initialize game variables
def init_vars():
    global player_position, direction
    player_position = [screen_width // 2, screen_height // 2]
    direction = "UP"

# Initialize game variables
init_vars()


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
            if event.key == pygame.K_UP and player_position[1] - player_step >= 0:
                player_position[1] -= player_step # moves player up by 20 pixels
            elif event.key == pygame.K_DOWN and player_position[1] - player_step <= screen_height:
                player_position[1] += player_step
            elif event.key == pygame.K_LEFT and player_position[0] - player_step >= 0:
                player_position[0] -= player_step
            elif event.key == pygame.K_RIGHT and player_position[0] and player_step <= screen_width:
                player_position[0] += player_step
                
    

    
    # Graphics
    screen.fill(BLACK)
    
    for pos in player_position:
        pygame.draw.circle(screen, YELLOW, player_position, circle_radius)
    
        
    
    # Update the display
    pygame.display.flip()