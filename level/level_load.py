# entities
from entities.player import Player
from entities.wall import Wall
from entities.block import Block
from entities.enemy import Enemy
from entities.gem import Gem
from entities.teleport import Teleport
# from entities.stairs import Stairs
from entities.wall_gray import WallGray
# from entities.door import Door
from entities.key import Key


from constants import (
    LIGHTGRAY,
    BLACK
)
from entities.player import Player
from renderer.cell import Cell
# from level_load import load_level

current_level_num = 1

def increase_level_num():
    global current_level_num
    current_level_num +=2
    return current_level_num
# crashes after level 20 obviously, and it needs to be reset if player wants to restore

class Stairs(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.image.fill(LIGHTGRAY)
        self.load_dos_char(240, BLACK)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            del_level()
            load_level(increase_level_num())
            print("To the next level!")
            return False

        return False

# place entities
from renderer.cell_grid import CellGrid
from constants import (
    BLACK,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GRID_CELL_HEIGHT,
    GRID_CELL_WIDTH,
)

from level.level_data import level_data

import pickle


game = CellGrid(
        grid_size=(GAME_GRID_COLS, GAME_GRID_ROWS),
        offset=(GRID_CELL_WIDTH, GRID_CELL_HEIGHT),
        fill=BLACK
    )


tile_mapping = {
    "P": Player,
    "#": Wall,
    "X": Block,
    "1": Enemy,
    "+": Gem,
    "T": Teleport,
    "L": Stairs,
    "6": WallGray,
    # "D": Door,
    "K": Key,
    " ": None
    }

    
def load_level(level_num):
    entity_pos = []
    for tile_key, tile_value in tile_mapping.items():
            for i, row in enumerate(level_data[f"level_{level_num}"]):
                for j, level_value in enumerate(row):
                    if level_value == tile_key and tile_value is not None:
                        entity_pos.append(game.put((j, i), tile_value()))
    for i in range(len(entity_pos)):
        return entity_pos[i]
        

def save_level():
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            entity = game.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i,j)))  
    with open("level.pkl", "wb") as f:
        pickle.dump(saved_level, f)

def del_level():
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            entity = game.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i,j)))  
    with open("current_level.pkl", "wb") as f:
        pickle.dump(saved_level, f)
    with open("current_level.pkl", "rb") as f:
        saved_level = pickle.load(f)
   
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
                game.remove((j, i))

def restore_level():
    del_level()
    with open("level.pkl", "rb") as f:
        saved_level = pickle.load(f)
        
    entity_classes = {
        "Player": Player,
        "Wall": Wall,
        "Block": Block,
        "Enemy": Enemy,
        "Gem": Gem,
        "Teleport": Teleport,
        "Stairs": Stairs,
        "WallGray": WallGray,
        # "Door": Door,
        "Key": Key
    }
    
    for entity_type, (i, j) in saved_level:
        if entity_type in entity_classes:
            game.put((j, i), entity_classes[entity_type]()) 

