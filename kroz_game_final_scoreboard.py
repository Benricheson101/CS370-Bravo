import pygame
pygame.init()
import random
import pygame.freetype
from enum import Enum
from dataclasses import dataclass
from typing import Optional, Tuple, Dict
import winsound, sys

def beep(a: int, b: int):
    if sys.platform == "win32":
        import winsound
        winsound.Beep(a, b)

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Constants
TILE_SIZE = 32
GRID_WIDTH = 28
GRID_HEIGHT = 20
SCOREBOARD_WIDTH = 13
SCREEN_WIDTH = (GRID_WIDTH + SCOREBOARD_WIDTH) * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE
SCOREBOARD_BEGIN = GRID_WIDTH * TILE_SIZE
FPS = 60

# Colors
COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'brown': (100, 50, 0),
    'gray': (128, 128, 128)
}

class TileType(Enum):
    VOID = -1
    EMPTY = 0
    WALL = 1
    GEM = 2
    ENEMY_SLOW = 3
    ENEMY_MEDIUM = 4
    ENEMY_FAST = 5
    STAIRS = 6
    PLAYER = 7
    TELEPORT = 8
    CHAR = 8

class Tile:
    def __init__(self, tile_type: TileType, walkable: bool = True, symbol: str = " "):
        self.type = tile_type
        self.walkable = walkable
        self.symbol = symbol
        self.color = COLORS['white']
   
    def render(self, surface: pygame.Surface, x: int, y: int, tile_size: int):
        pass

class VoidTile(Tile):
    def __init__(self):
        super().__init__(TileType.VOID, False, "")

class EmptyTile(Tile):
    def __init__(self):
        super().__init__(TileType.EMPTY, True, " ")

class WallTile(Tile):
    def __init__(self):
        super().__init__(TileType.WALL, False, "█")
        self.color = COLORS['brown']
   
    def render(self, surface: pygame.Surface, x: int, y: int, tile_size: int):
        pygame.draw.rect(surface, self.color,
                        (x * tile_size, y * tile_size, tile_size, tile_size))

class GemTile(Tile):
    def __init__(self):
        super().__init__(TileType.GEM, True, "◊")  # Match the enemy tile's appearance
        self.color = COLORS['cyan']
   
    def render(self, surface: pygame.Surface, x: int, y: int, tile_size: int):
        font = pygame.font.Font(None, tile_size)
        text = font.render(self.symbol, True, self.color)
        text_rect = text.get_rect(center=(x * tile_size + tile_size // 2,
                                          y * tile_size + tile_size // 2))
        surface.blit(text, text_rect)


class TeleportTile(Tile):
    def __init__(self):
            super().__init__(TileType.TELEPORT, True, "T")
            self.color = COLORS['magenta']
        
    def render(self, surface: pygame.SurfaceType, x: int, y: int, tile_size: int):
        font = pygame.font.Font(None, tile_size)
        text = font.render(self.symbol, True, self.color)
        text_rect = text.get_rect(center=(x * tile_size + tile_size//2,
                                        y * tile_size + tile_size//2))
        surface.blit(text, text_rect)
        
#
#
#Changed Walkable to true
class EnemyTile(Tile):
    def __init__(self, enemy_type: TileType, symbol: str, color: Tuple[int, int, int]):
        super().__init__(enemy_type, True, symbol)
        self.color = color
   
    def render(self, surface: pygame.Surface, x: int, y: int, tile_size: int):
        font = pygame.font.Font(None, tile_size)
        text = font.render(self.symbol, True, self.color)
        text_rect = text.get_rect(center=(x * tile_size + tile_size//2,
                                        y * tile_size + tile_size//2))
        surface.blit(text, text_rect)
        
class CharTile(Tile):
    def __init__(self, char: str, fg = COLORS['white'], bg = COLORS['blue']):
        super().__init__(TileType.CHAR, False, char)
        self.char = char
        self.fg = fg
        self.bg = bg
        # self.fg = COLORS['white']
        # self.bg = COLORS['blue']

    def render(self, surface: pygame.Surface, x: int, y: int, tile_size: int):
        font = pygame.freetype.SysFont(["Perfect DOS VGA 437", "Courier New"], tile_size, bold=True)
        text_surface, _ = font.render(self.char, fgcolor=self.fg, bgcolor=self.bg)

        # text_rect = text_surface.convert_alpha().get_rect(center=(x * tile_size + tile_size//2,
        #                                 y * tile_size + tile_size//2))

        # FIXME: some letters (p, g, j) are positioned weirdly
        text_rect = text_surface.convert_alpha().get_rect(midbottom=(x * tile_size + tile_size//2,
        y * tile_size + int(tile_size * (7/8)))) # 7/8 is weird but it looks okay, idk if there's a standard we should follow or now
        surface.blit(text_surface, text_rect)


class TileMap:
    def __init__(self, width: int, height: int):
        self.tiles = [[EmptyTile() for _ in range(height)] for _ in range(width)]
        self.width = width
        self.height = height
   
    def get_width(self) -> int:
        return self.width
   
    def get_height(self) -> int:
        return self.height
   
    def get_tile(self, x: int, y: int) -> Tile:
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return VoidTile()
        return self.tiles[x][y]
    
    def get_random_empty_tile(self) -> Optional[Tuple[int, int]]:
        """Finds and returns a random empty tile's coordinates."""
        empty_tiles = []
        for x in range(self.width):
            for y in range(self.height):
                if isinstance(self.tiles[x][y], EmptyTile):
                    empty_tiles.append((x, y))

        if empty_tiles:  # Check if any empty tiles were found
            return random.choice(empty_tiles)
        

    def set_tile(self, x: int, y: int, tile: Tile):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[x][y] = tile
   
    def render(self, surface: pygame.Surface, tile_size: int):
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[x][y].render(surface, x, y, tile_size)


class Scoreboard(TileMap):
    def __init__(self):
        super().__init__(SCOREBOARD_WIDTH, GRID_HEIGHT)
        self.score = 0

    def set_score(self, new_score: int):
        self.score = new_score

    def set_text(self, text: str, start_pos: tuple[int, int], fg = COLORS['white'], bg = COLORS['blue']):
        for i, c in enumerate(text):
            self.set_tile(start_pos[0] + i, start_pos[1], CharTile(c, fg, bg))

    def render(self, surface: pygame.Surface, tile_size: int):
        sb = pygame.Surface((SCOREBOARD_WIDTH * TILE_SIZE, SCREEN_HEIGHT))
        rect = sb.get_rect(topleft=(SCOREBOARD_BEGIN, 0))

        sb.fill(COLORS['blue'])

        self.set_text("Score", (4, 0), fg=COLORS['yellow'])
        for i in range(3, 10):
            self.set_tile(i, 1, WallTile())

        # self.set_text("Level", (4, 3), fg=COLORS['yellow'])
        # for i in range(3, 10):
        #     self.set_tile(i, 4, WallTile())

        self.set_text("Gems", (4, 6), fg=COLORS['yellow'])
        for i in range(3, 10):
            self.set_tile(i, 7, WallTile())

        # self.set_text("Whips", (4, 9), fg=COLORS['yellow'])
        # for i in range(3, 10):
        #     self.set_tile(i, 10, WallTile())

        # self.set_text("Teleports", (2, 12), fg=COLORS['yellow'])
        # for i in range(3, 10):
        #     self.set_tile(i, 13, WallTile())


        super().render(sb, tile_size)
        surface.blit(sb, rect)

class KrozGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Team Bravo Kroz Game")
        self.clock = pygame.time.Clock()
       
        # Create tile map
        self.tile_map = TileMap(GRID_WIDTH, GRID_HEIGHT)
        
        self.scoreboard = Scoreboard()
       
        # Player position
        self.player_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
       
        # Game state
        self.score = 0
        self.level = 1
        
        # Gem count
        self.gem = 10
       
        # Initialize level
        self.init_level()

    def init_level(self):
        # Create walls around the border
        for x in range(GRID_WIDTH):
            self.tile_map.set_tile(x, 0, WallTile())
            self.tile_map.set_tile(x, GRID_HEIGHT-1, WallTile())
       
        for y in range(GRID_HEIGHT):
            self.tile_map.set_tile(0, y, WallTile())
            self.tile_map.set_tile(GRID_WIDTH-1, y, WallTile())
       
        # Add random elements
        for x in range(1, GRID_WIDTH-1):
            for y in range(1, GRID_HEIGHT-1):
                rand = random.random()
                if rand < 0.1:
                    self.tile_map.set_tile(x, y, WallTile())
                elif rand < 0.15:
                    self.tile_map.set_tile(x, y, GemTile())
                elif rand < 0.18:
                    enemy_type = random.choice([
                        (TileType.ENEMY_SLOW, "○", COLORS['red']),
                        (TileType.ENEMY_MEDIUM, "◊", COLORS['green']),
                        (TileType.ENEMY_FAST, "△", COLORS['blue'])
                    ])
                    self.tile_map.set_tile(x, y, EnemyTile(*enemy_type))
               
                elif rand < .14:
                    self.tile_map.set_tile(x,y, TeleportTile())

    def handle_input(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        # Get the state of all keys
        keys = pygame.key.get_pressed()
        new_pos = self.player_pos.copy()
        
        # Movement delay variables
        MOVE_DELAY = 150  # Delay in milliseconds (higher = slower)
        current_time = pygame.time.get_ticks()
        
        if not hasattr(self, "last_move_time"):
            self.last_move_time = 0  # Initialize movement time
        if current_time - self.last_move_time > MOVE_DELAY:
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
                beep(150,20)
                beep(100,20)
            
            
            # Movement logic
            if keys[pygame.K_LEFT]:
                new_pos[0] -= 1
            elif keys[pygame.K_RIGHT]:
                new_pos[0] += 1
            elif keys[pygame.K_UP]:
                new_pos[1] -= 1
            elif keys[pygame.K_DOWN]:
                new_pos[1] += 1

                
            tile = self.tile_map.get_tile(new_pos[0], new_pos[1])
            if tile.walkable:
                if isinstance(tile, GemTile):
                    self.score += 10
                    self.gem += 1
                    self.tile_map.set_tile(new_pos[0], new_pos[1], EmptyTile())
                    beep(200,100)
                    # self.draw_message("gem")
                self.player_pos = new_pos

                if isinstance(tile, EnemyTile):
                    
                    self.tile_map.set_tile(new_pos[0], new_pos[1], EmptyTile())
                    beep(300,100)
                    self.draw_message("enemy")
                    if self.gem != 0:
                        self.gem -= 1
                self.player_pos = new_pos

                #Teleport
                if isinstance(tile, TeleportTile):
                    self.tile_map.set_tile(new_pos[0], new_pos[1], EmptyTile())
                    beep(200,100)
                    #move player to random empty tile
                    new_empty_tile = self.tile_map.get_random_empty_tile()
                    if new_empty_tile:
                        self.player_pos = list(new_empty_tile)
                    
                



            elif self.score > 10:
                self.score -= 10 # Player loses points for running into wall
                beep(100,10)
                beep(150,1)
            else:
                beep(100,10)
                beep(150,1)
                self.draw_message("wall")
                
                
            
            # Update the last movement time
            self.last_move_time = current_time
       
        return True
    
    # Message if player runs into wall
    def draw_message(self, message):
        font = pygame.font.Font(None, 36)
        if message == "wall":
            wall_text = font.render(f'A Solid Wall blocks your way', True, COLORS['white'])
            self.screen.blit(wall_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT - 30))
        elif message == "gem":
            gem_text = font.render(f'Gems give you both points and strength', True, COLORS['white'])
            self.screen.blit(gem_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT - 30))
        
        pygame.display.flip()
        pygame.time.delay(700)
    
    def draw(self):
        self.screen.fill(COLORS['black'])
       
        # Draw tilemap
        self.tile_map.render(self.screen, TILE_SIZE)
        
        self.scoreboard.render(self.screen, TILE_SIZE)
       
        # Draw player
        pygame.draw.circle(self.screen, COLORS['yellow'],
                         (self.player_pos[0] * TILE_SIZE + TILE_SIZE//2,
                          self.player_pos[1] * TILE_SIZE + TILE_SIZE//2),
                         TILE_SIZE//3)
       
        # Draw UI
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'{self.score}', True, COLORS['white'])
        # level_text = font.render(f'Level: {self.level}', True, COLORS['white'])
        gem_text = font.render(f'{self.gem}', True, COLORS['white'])
       
        self.screen.blit(score_text, (1100, 40))
        # self.screen.blit(level_text, (10, 50))
        self.screen.blit(gem_text, (1100, 230))
       
        pygame.display.flip()

########################################################
    def move_enemies(self):
        for x in range(self.tile_map.width):
            for y in range(self.tile_map.height):
                tile = self.tile_map.get_tile(x, y)
                if isinstance(tile, EnemyTile):
                    self.move_enemy(x, y, tile)

    def move_enemy(self, x, y, enemy_tile):
        dx = self.player_pos[0] - x
        dy = self.player_pos[1] - y

        # Prioritize vertical movement
        if abs(dy) > abs(dx):
            if dy > 0:  # Player below
                new_y = y + 1
                if self.tile_map.get_tile(x, new_y).walkable and not isinstance(self.tile_map.get_tile(x, new_y), EnemyTile):
                    self.tile_map.set_tile(x, y, EmptyTile())
                    self.tile_map.set_tile(x, new_y, enemy_tile)
                    return  # Enemy has moved, exit

            elif dy < 0:  # Player above
                new_y = y - 1
                if self.tile_map.get_tile(x, new_y).walkable and not isinstance(self.tile_map.get_tile(x, new_y), EnemyTile):
                    self.tile_map.set_tile(x, y, EmptyTile())
                    self.tile_map.set_tile(x, new_y, enemy_tile)
                    return # Enemy has moved, exit

        # If vertical move not possible or not prioritized, try horizontal
        if abs(dx) > 0: # Check if horizontal movement is needed
            if dx > 0:  # Player to the right
                new_x = x + 1
                if self.tile_map.get_tile(new_x, y).walkable and not isinstance(self.tile_map.get_tile(new_x, y), EnemyTile):
                    self.tile_map.set_tile(x, y, EmptyTile())
                    self.tile_map.set_tile(new_x, y, enemy_tile)
                    return # Enemy has moved, exit

            elif dx < 0:  # Player to the left
                new_x = x - 1
                if self.tile_map.get_tile(new_x, y).walkable and not isinstance(self.tile_map.get_tile(new_x, y), EnemyTile):
                    self.tile_map.set_tile(x, y, EmptyTile())
                    self.tile_map.set_tile(new_x, y, enemy_tile)
                    return # Enemy has moved, exit
##################################################################################

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.move_enemies() # Move enemies every frame
            self.draw()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = KrozGame()
    game.run()