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
    entity_pos = []
    for tile_key, tile_value in tile_mapping.items():
            for i, row in enumerate(level_data[f"level_{level_num}"]):
                for j, level_value in enumerate(row):
                    if level_value == tile_key and tile_value is not None:
                        entity_pos.append(game.remove((j, i)))
    for i in range(len(entity_pos)):
        return entity_pos[i]

    
  
  
