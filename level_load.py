# idk

# entities
from entities.player import Player
from entities.wall import Wall
from entities.block import Block
from entities.enemy import Enemy
from entities.gem import Gem
from entities.teleport import Teleport

# place entities
from renderer.cell_grid import CellGrid
from constants import (
    BLACK,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GRID_CELL_HEIGHT,
    GRID_CELL_WIDTH,
)

from level_data import level_data



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
    " ": None
    }



def load_gem():
    gem_pos = []
    for i, row in enumerate(level_data[f"level_1"]):
        for j, value in enumerate(row):
            if value == "+":
                gem_pos.append(game.put((j, i), Gem()))
    for i in range(len(gem_pos)):
        return gem_pos[i]
    
def load_wall():
    wall_pos = []
    for i, row in enumerate(level_data[f"level_1"]):
        for j, value in enumerate(row):
            if value == "#":
                wall_pos.append(game.put((j, i), Wall()))
    for i in range(len(wall_pos)):
        return wall_pos[i]

# iterate through dictionary
# for key in tile_mapping.keys():
#     print(key)
   
# for value in tile_mapping.values():
#     print(value)
    
# for key, value in tile_mapping.items():
#     print(key, value)
    
def load_level():
    entity_pos = []
    for tile_key, tile_value in tile_mapping.items():
            for i, row in enumerate(level_data[f"level_1"]):
                for j, level_value in enumerate(row):
                    if level_value == tile_key and tile_value is not None:
                        entity_pos.append(game.put((j, i), tile_value()))
    for i in range(len(entity_pos)):
        return entity_pos[i]
    

    
  
  
