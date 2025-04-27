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
from entities.cwall2 import CWall2
from entities.cspell2 import CSpell2
from entities.cwall3 import CWall3
from entities.cspell3 import CSpell3
from entities.forest import Forest
from entities.tree import Tree
from entities.power import Power
from entities.tunnel import Tunnel
from entities.crown import Crown
from entities.ospell1 import OSpell1
from entities.owall1 import OWall1
from entities.ospell2 import OSpell2
from entities.owall2 import OWall2
from entities.ospell3 import OSpell3
from entities.owall3 import OWall3
from entities.gblock import GBlock
from entities.zblock import ZBlock
from entities.blockspell import BlockSpell





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
    "7": CWall1,
    "ô": CSpell1,
    "8": CWall2,
    "õ": CSpell2,
    "9": CWall3,
    "ö": CSpell3,
    "/": Forest,
    "\\": Tree,
    "Q": Power,
    "U": Tunnel,
    "A": Crown,
    "4": OWall1,
    "5": OWall2,
    "6": OWall3,
    "ñ": OSpell1,
    "ò": OSpell2,
    "ó": OSpell3,
    "Y": GBlock,
    "O": ZBlock,
    "H": BlockSpell
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
    elif Tile is not None:
        return Tile()
    elif char.isalnum() and char.islower():
        return Char(char.upper(), fg=WHITE, bg=BROWN)
    

def load_level(game: "Game", grid: CellGrid, level_num: int):
    for i, row in enumerate(level_data[f"level_{level_num}"]):
        for j, level_value in enumerate(row):
            tile = char_to_tile(level_value, game)
            if tile is not None:
                grid.put((j+1, i+1), tile)


def save_level(grid: CellGrid):
    saved_level = []
    for i in range(1, GAME_GRID_ROWS + 1):  # start at 1 because border
        for j in range(1, GAME_GRID_COLS + 1):
            entity = grid.grid[i][j]
            if entity is not None:
                entity_type = entity.__class__.__name__
                saved_level.append((entity_type, (i, j)))  # save positions
    
    save_data = {
        "level_data": saved_level,
        "score": game_instance.score,
        "current_level": game_instance.current_level,
        "key_count": game_instance.key_count,
        "gem_count": game_instance.gem_count,
        "whip_count": game_instance.whip_count,
        "teleport_count": game_instance.teleport_count,
        "whip_power": game_instance.whip_power,
        "difficulty": game_instance.difficulty
    }
    with open("level/level.pkl", "wb") as f:
        pickle.dump(save_data, f)



def del_level(grid: CellGrid):
    for i in range(1, GAME_GRID_ROWS + 1):
        for j in range(1, GAME_GRID_COLS + 1):
            grid.remove((j, i))

    for i in range(GAME_GRID_ROWS):
        for j in range(GAME_GRID_COLS):
            grid.remove((j, i))


def restore_level(grid: CellGrid):
    grid.clrscr()
    with open("level/level.pkl", "rb") as f:
        save_data = pickle.load(f)
        
    # Restore score and items
    game_instance.score = save_data.get("score", 0)
    game_instance.current_level = save_data.get("current_level", 1)
    game_instance.key_count = save_data.get("key_count", 0)
    game_instance.gem_count = save_data.get("gem_count", 0)
    game_instance.whip_count = save_data.get("whip_count", 0)
    game_instance.teleport_count = save_data.get("teleport_count", 0)
    game_instance.whip_power = save_data.get("whip_power", 2)
    game_instance.difficulty = save_data.get("difficulty", 8)
    
    saved_level = save_data["level_data"]
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
        "CSpell1": CSpell1,
        "CWall2": CWall2,
        "CSpell2": CSpell2,
        "CWall3": CWall3,
        "CSpell3": CSpell3,
        "Forest": Forest,
        "Tree": Tree,
        "Power": Power,
        "Tunnel": Tunnel,
        "Crown": Crown,
        "OWall1": OWall1,
        "OWall2": OWall2,
        "OWall3": OWall3,
        "OSpell1": OSpell1,
        "OSpell2": OSpell2,
        "OSpell3": OSpell3,
        "GBlock": GBlock,
        "ZBlock": ZBlock,
        "BlockSpell": BlockSpell
    }

    for entity_type, (i, j) in saved_level:
        if entity_type in entity_classes:
            if entity_type in ("Gem", "Nugget"):
                entity = Gem(game_instance.gem_color) if entity_type == "Gem" else Nugget(game_instance.art_color)
            else:
                entity = entity_classes[entity_type]()
            grid.put((j, i), entity)  # no +1 now
                
    grid.border()



from level.level_data_random import level_data_random

def random_level(grid: CellGrid, level_num: int):
    level_key = f"level_{level_num}"

    if level_key not in level_data_random:
        print(f"Warning: No random object data for level {level_num}")
        return

    data = level_data_random[level_key]
    object_counts = data["object_counts"]

    # Place Player first
    player_pos = data.get("player_pos")
    if player_pos:
        x, y = player_pos
        from entities.player import Player  # Import if not already
        player = Player()
        grid.put((x, y), player)
        if game_instance:
            game_instance.player = player

    # Place other objects randomly
    for obj_char, count in object_counts.items():
        entity_class = tile_mapping.get(obj_char)

        if entity_class is None:
            print(f"Warning: No entity mapped for '{obj_char}'")
            continue

        for _ in range(count):
            try:
                x, y = grid.get_random_empty_tiles()
                if entity_class is Gem:
                    entity = entity_class(game_instance.gem_color)
                elif entity_class is Nugget:
                    entity = entity_class(game_instance.art_color)
                else:
                    entity = entity_class()
                grid.put((x, y), entity)
            except ValueError:
                print("Warning: No empty tiles left to place entity!")
                break




