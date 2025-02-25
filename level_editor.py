import pygame, sys

# Initialize Pygame and check for errors
check_errors = pygame.init()
#check_errors[1] is the second tuple of pygame.init() which contains number of errors
if check_errors[1] > 0:
    print("Error " + check_errors[1])
else:
    print("Game Successfully initialized")


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kroz Level Editor")
PLAYER_RADIUS = 20
SPEED = 5


WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

player_pos = [ screen_width// 2, screen_height // 2]


while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_pos[0] -= SPEED  # Move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += SPEED  # Move right
    if keys[pygame.K_UP]:
        player_pos[1] -= SPEED  # Move up
    if keys[pygame.K_DOWN]:
        player_pos[1] += SPEED  # Move down
    
    # Prevent the player from going out of bounds
    player_pos[0] = max(min(player_pos[0], screen_width - PLAYER_RADIUS), PLAYER_RADIUS)
    player_pos[1] = max(min(player_pos[1], screen_height - PLAYER_RADIUS), PLAYER_RADIUS)
    
    # Draw the player (circle)
    pygame.draw.circle(screen, YELLOW, player_pos, PLAYER_RADIUS)
    
    # Update the display
    pygame.display.flip()
    
