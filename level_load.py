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
        
        
def del_level(level_num):
    for tile_key, tile_value in tile_mapping.items():
            for i, row in enumerate(level_data[f"level_{level_num}"]):
                for j, level_value in enumerate(row):
                    if level_value == tile_key and tile_value is not None:
                        game.remove((j, i))
                        


def save_level():
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
                saved_level.append(game.grid[i][j])
    with open("level.pkl", "wb") as f:
        pickle.dump(saved_level, f)

def restore_level():
    with open("level.pkl", "rb") as f:
        level = pickle.load(f)
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            game.put((i,j), level[i][j])

def del_level():
    return None
                        



    
    
  
  
