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
pygame.display.set_caption("Kroz")

TILE_SIZE = 40
player_radius = TILE_SIZE // 3

# Colors
COLORS = {
    'yellow': (255, 255, 0),
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'grid': (50, 50, 50)
}

# Movement constants from Kroz
MOVE_NORTH = 172
MOVE_SOUTH = 180
MOVE_EAST = 177
MOVE_WEST = 175
MOVE_NORTHWEST = 171
MOVE_NORTHEAST = 173
MOVE_SOUTHWEST = 179
MOVE_SOUTHEAST = 181

# Create the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kroz")

class Player:
    def __init__(self):
        self.grid_x = 5  # Starting position from provided code
        self.grid_y = 5
        self.moving = False
        self.move_cooldown = 0
        self.MOVE_DELAY = 150

    def move(self, direction):
        if self.moving or self.move_cooldown > 0:
            return

        dx = dy = 0

        # Movement based on Kroz directional constants
        if direction == MOVE_NORTH:
            dy = -1
        elif direction == MOVE_SOUTH:
            dy = 1
        elif direction == MOVE_EAST:
            dx = 1
        elif direction == MOVE_WEST:
            dx = -1
        elif direction == MOVE_NORTHWEST:
            dx, dy = -1, -1
        elif direction == MOVE_NORTHEAST:
            dx, dy = 1, -1
        elif direction == MOVE_SOUTHWEST:
            dx, dy = -1, 1
        elif direction == MOVE_SOUTHEAST:
            dx, dy = 1, 1

        # Calculate new position
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy

        # Check grid boundaries
        max_grid_x = (screen_width // TILE_SIZE) - 1
        max_grid_y = (screen_height // TILE_SIZE) - 1

        if 0 <= new_x <= max_grid_x and 0 <= new_y <= max_grid_y:
            self.grid_x = new_x
            self.grid_y = new_y
            self.moving = True
            self.move_cooldown = self.MOVE_DELAY

            # Play movement sound
            
            

    def update(self, dt):
        if self.move_cooldown > 0:
            self.move_cooldown -= dt
        else:
            self.moving = False

    def draw(self, surface):
        player_x = self.grid_x * TILE_SIZE + TILE_SIZE // 2
        player_y = self.grid_y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(surface, COLORS['yellow'], (player_x, player_y), player_radius)

def draw_grid():
    for x in range(0, screen_width, TILE_SIZE):
        for y in range(0, screen_height, TILE_SIZE):
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, COLORS['grid'], rect, 1)

# Create a simple movement sound
#move_sound = pygame.mixer.Sound(bytes(bytearray([128] * 1000)))
#move_sound.set_volume(0.1)

def main():
    clock = pygame.time.Clock()
    player = Player()
    last_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        dt = current_time - last_time
        last_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not player.moving:
                keys = pygame.key.get_pressed()

                # Handle diagonal movement first
                if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                    player.move(MOVE_NORTHWEST)
                elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                    player.move(MOVE_NORTHEAST)
                elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                    player.move(MOVE_SOUTHWEST)
                elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                    player.move(MOVE_SOUTHEAST)
                # Handle cardinal movement
                elif keys[pygame.K_UP]:
                    player.move(MOVE_NORTH)
                elif keys[pygame.K_DOWN]:
                    player.move(MOVE_SOUTH)
                elif keys[pygame.K_LEFT]:
                    player.move(MOVE_WEST)
                elif keys[pygame.K_RIGHT]:
                    player.move(MOVE_EAST)

        # Update
        player.update(dt)

        # Drawing
        screen.fill(COLORS['black'])
        draw_grid()
        player.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()
