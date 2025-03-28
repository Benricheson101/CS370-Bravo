# entities
from entities.player import Player
from entities.wall import Wall
from entities.block import Block
from entities.enemy import Enemy
from entities.gem import Gem
from entities.whip import Whip
from entities.teleport import Teleport
from entities.stairs import Stairs
from entities.wall_gray import WallGray
from entities.door import Door
from entities.key import Key





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

game_instance = None

def set_game_instance(game):
    global game_instance
    game_instance = game  # Store reference to Game



tile_mapping = {
    "P": Player,
    "#": Wall,
    # "X": Block,
    "1": Enemy,
    "+": Gem,
    "T": Teleport,
    "L": Stairs,
    "6": WallGray,
    "D": Door,
    "K": Key,
    "W": Whip,
    " ": None
    }


def load_level(game, level_num):
    entity_pos = []
    for tile_key, tile_value in tile_mapping.items():
            for i, row in enumerate(level_data[f"level_{level_num}"]):
                for j, level_value in enumerate(row):
                    if level_value == tile_key and tile_value is not None:
                        entity = tile_value(game.game.gem_color) if tile_value == Gem else tile_value()
                        entity_pos.append(game.put((j+1, i+1), entity))
    for i in range(len(entity_pos)):
        return entity_pos[i]


def save_level(game):
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            entity = game.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i,j)))
    with open("level/level.pkl", "wb") as f:
        pickle.dump(saved_level, f)

def del_level(game):
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            entity = game.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i,j)))
    with open("level/current_level.pkl", "wb") as f:
        pickle.dump(saved_level, f)
    with open("level/current_level.pkl", "rb") as f:
        saved_level = pickle.load(f)

    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
                game.remove((j, i))

def restore_level(game):
    del_level(game)
    with open("level/level.pkl", "rb") as f:
        saved_level = pickle.load(f)

    entity_classes = {
        "Player": Player,
        "Wall": Wall,
        # "Block": Block,
        "Enemy": Enemy,
        "Gem": Gem,
        "Teleport": Teleport,
        "Stairs": Stairs,
        "WallGray": WallGray,
        "Door": Door,
        "Key": Key,
        "Whip": Whip
    }

    for entity_type, (i, j) in saved_level:
        if entity_type in entity_classes:
            game.put((j+1, i+1), entity_classes[entity_type]())
            
            




object_counts = {
    "P": 1,
    "#": 0,
    # "X": 50,
    "1": 100,
    "+": 200,
    "T": 50,
    "L": 2,
    "6": 0,
    "D": 0,
    "K": 0,
    "W": 20
}

def random_level(grid: CellGrid, level_num, object_counts):
   
    for obj_char, count in object_counts.items():
        entity_class = tile_mapping.get(obj_char)

        if entity_class is None:
            print(f"Warning: No entity mapped for '{obj_char}'")
            continue

        # Place entities using random empty tiles
        for _ in range(count):
            x, y = grid.get_random_empty_tiles(grid)

            # Create the correct entity and place it
            entity = entity_class() if entity_class != Gem else entity_class(grid.game.gem_color)
            grid.put((x, y), entity)
            
