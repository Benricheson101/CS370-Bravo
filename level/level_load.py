# entities
from entities.player import Player
from entities.wall import Wall
from entities.block import Block
from entities.enemy import Enemy
from entities.enemy_medium import Enemy_Medium
from entities.enemy_hard import Enemy_Hard
from entities.gem import Gem
from entities.whip import Whip
from entities.teleport import Teleport
from entities.stairs import Stairs
from entities.wall_gray import WallGray
from entities.door import Door
from entities.key import Key
from entities.spell_freeze import Spell_Freeze
from entities.spell_zap import Spell_Zap





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


current_level_num = 1

def increase_level_num():
    global current_level_num
    current_level_num +=2
    return current_level_num
# crashes after level 20 obviously, and it needs to be reset if player wants to restore
# for some reason testing door/key in level 9, stairs takes it to level 2???

tile_mapping = {
    "P": Player,
    "#": Wall,
    "X": Block,
    "1": Enemy,
    "2": Enemy_Medium,
    "3": Enemy_Hard,
    "Z": Spell_Freeze,
    "%": Spell_Zap,
    "+": Gem,
    "T": Teleport,
    "L": Stairs,
    "6": WallGray,
    # "D": Door,
    "K": Key,
    "W": Whip,
    " ": None
    }


def load_level(game, level_num):
    #global instance call
    global game_instance
    entity_pos = []
    for tile_key, tile_value in tile_mapping.items():
            for i, row in enumerate(level_data[f"level_{level_num}"]):
                for j, level_value in enumerate(row):
                    if level_value == tile_key and tile_value is not None:
                        if tile_value == Player:
                            player_instance = Player()
                            entity = player_instance
                            game_instance.player = player_instance
                        elif tile_value == Gem:
                            entity = tile_value(game.game.gem_color)
                        elif tile_value == Enemy:
                            entity = Enemy(player=game_instance.player)
                        elif tile_value == Enemy_Medium:
                            entity = Enemy_Medium(player=game_instance.player)
                        elif tile_value == Enemy_Hard:
                            entity = Enemy_Hard(player=game_instance.player)
                        else:
                            entity = tile_value()
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
        "Block": Block,
        "Enemy": Enemy,
        "Enemy_Medium": Enemy_Medium,
        "Gem": Gem,
        "Teleport": Teleport,
        "Stairs": Stairs,
        "WallGray": WallGray,
        # "Door": Door,
        "Key": Key,
        "Whip": Whip
    }

    for entity_type, (i, j) in saved_level:
        if entity_type in entity_classes:
            game.put((j+1, i+1), entity_classes[entity_type]())

