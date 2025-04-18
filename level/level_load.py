# entities
from typing import TYPE_CHECKING, Optional
from entities.char import Char
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
from entities.invisible import Invisible
from entities.nugget import Nugget
from entities.river import River
from entities.show_gems import ShowGems
from entities.spell_freeze import Spell_Freeze
from entities.spell_zap import Spell_Zap
from entities.lava import Lava
from entities.iwall import IWall
from entities.iblock import IBlock
from entities.cwall1 import CWall1
from entities.cspell1 import CSpell1





# place entities
if TYPE_CHECKING:
    from game import Game
from renderer.cell import Cell
from renderer.cell_grid import CellGrid
from constants import (
    BLACK,
    BROWN,
    GAME_GRID_COLS,
    GAME_GRID_ROWS,
    GRID_CELL_HEIGHT,
    GRID_CELL_WIDTH,
    WHITE,
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
    "X": Block,
    "1": Enemy,
    "2": Enemy_Medium,
    "3": Enemy_Hard,
    "+": Gem,
    "T": Teleport,
    "L": Stairs,
    "6": WallGray,
    "D": Door,
    "K": Key,
    "W": Whip,
    "I": Invisible,
    "*": Nugget,
    "R": River,
    "&": ShowGems,
    "Z": Spell_Freeze,
    "%": Spell_Zap,
    "V": Lava,
    ":": IWall,
    ";": IBlock,
    }

def char_to_tile(char: str, game: "Game") -> Optional["Cell"]:
    if char == " ":
        return None

    Tile: Optional["Cell"] = tile_mapping.get(char, None)
    if Tile is Gem:
        return Tile(game.gem_color)
    elif Tile is Nugget:
        return Tile(game.art_color)
    elif Tile is Player:
        player = Tile()
        game.player = player
        return player
    elif char.isalnum() and char.islower():
        return Char(char.upper(), fg=WHITE, bg=BROWN)
    elif Tile is not None:
        return Tile()

def load_level(game: "Game", grid: CellGrid, level_num: int):
    for i, row in enumerate(level_data[f"level_{level_num}"]):
        for j, level_value in enumerate(row):
            tile = char_to_tile(level_value, game)
            if tile is not None:
                grid.put((j+1, i+1), tile)


def save_level(grid: CellGrid):
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            entity = grid.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i,j)))
    with open("level/level.pkl", "wb") as f:
        pickle.dump(saved_level, f)

def del_level(grid: CellGrid):
    saved_level = []
    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            entity = grid.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i,j)))
    with open("level/current_level.pkl", "wb") as f:
        pickle.dump(saved_level, f)
    with open("level/current_level.pkl", "rb") as f:
        saved_level = pickle.load(f)

    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            grid.remove((j, i))


def restore_level(grid: CellGrid):
    del_level(grid)
    with open("level/level.pkl", "rb") as f:
        saved_level = pickle.load(f)

    entity_classes = {
        "Player": Player,
        "Wall": Wall,
        "Block": Block,
        "Enemy": Enemy,
        "Enemy_Medium": Enemy_Medium,
        "Enemy_Hard": Enemy_Hard,
        "Gem": Gem,
        "Teleport": Teleport,
        "Stairs": Stairs,
        "WallGray": WallGray,
        "Door": Door,
        "Key": Key,
        "Whip": Whip,
        "Invisible": Invisible,
        "Nugget": Nugget,
        "River": River,
        "ShowGems": ShowGems,
        "IWall": IWall,
        "IBlock": IBlock,
        "CWall1": CWall1,
        "CSpell1": CSpell1
    }

    for entity_type, (i, j) in saved_level:
        if entity_type in entity_classes:
            if entity_type in ("Gem", "Nugget"):
                entity = Gem(game_instance.gem_color)
            else:
                entity = entity_classes[entity_type]()
            grid.put((j+1, i+1), entity)








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
            x, y = grid.get_random_empty_tiles()

            # Create the correct entity and place it
            entity = entity_class() if entity_class != Gem else entity_class(game_instance.gem_color)
            grid.put((x, y), entity)


