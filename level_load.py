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


def get_entity_pos(list, dictionary):
    indexes = []
    for i, row in enumerate(list):
        for j, value in enumerate(row):
            if value in dictionary:
                indexes.append((j, i))
    return indexes



def load_level(level_num):
    entity_positions = []
    for i, row in enumerate(level_data[f"level_{level_num}"]):
        for j, value in enumerate(row):
            if value in tile_mapping:
                entity_positions.append(game.put((j, i), tile_mapping.get(value, None)))
    for i in range(len(entity_positions)):
        return entity_positions[i]
    
def load_gem(level_num):
    # empty list of gem_pos, which will store the game puts
    # see if there are any "+" in level_data...
    # when a "+" is found, append the gem_pos list with those index coordinates
    gem_pos = []
    for i, row in enumerate(level_data[f"level_{level_num}"]):
        for j, value in enumerate(row):
            if "+" in level_data[f"level_{level_num}"]:
                gem_pos.append(game.put(j,i), Gem())
    for i in range(len(gem_pos)):
        return gem_pos[i]
    
    # Gem_place = [
    #     game.put((20,20), Gem()),
    #     game.put((22,22), Gem()),
    #     game.put((24,22), Gem()),
    #     game.put((26,22), Gem()),
    #     game.put((28,22), Gem())
    # ]
    # for i in range(len(Gem_place)):
        
    #     return Gem_place[i]


if any("+" in line for line in level_data["level_1"]):
    print("yes")
else:
    print("no")
    
    
    
  
  
