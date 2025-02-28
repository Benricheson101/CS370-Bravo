from entities.wall import Wall
from entities.block import Block
from entities.enemy import Enemy
from entities.gem import Gem
from entities.teleport import Teleport


tile_mapping = {
    "#": Wall,
    "X": Block,
    "1": Enemy,
    "+": Gem,
    "T": Teleport
}

def load_level(level_num):
    return None

# Open the file in read mode
with open('levels/level_1.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    file.seek(0)
    print(file.readline())
# Print the content
print()
print()
# print(content)


