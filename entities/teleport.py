from constants import PINK
from entities.player import Player
from renderer.cell import Cell
from pygame import Vector2
import pygame
from renderer.cell_grid import CellGrid


class Teleport(Cell):
    def __init__(self) -> None:
        super().__init__()
        # self.load_sprite("./sprites/teleport.png")
        self.load_dos_char(24, PINK)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Player hit a Teleport scroll!")
            
            empty_cell = cell.grid.get_random_empty_tiles()
            if empty_cell:
                col, row = empty_cell  # Unpack the tuple into x and y
                print(f"Teleporting player to: {empty_cell}")
                
                

              #  Player.move_to(Teleport, (col,row), Player )
                Player.get_player_position(self)
                result = tuple(map(lambda i, j: j - i, Player.get_player_position(self), empty_cell))
                DVector = pygame.math.Vector2(result)
                print(DVector)

                Player.move(self, DVector) #moves the teleport object instead of the player... 

                

            return True

        return False