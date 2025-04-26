import random
from typing import Optional
from entities.player import Player
from renderer.cell import Cell
from renderer.cell_grid import CellGrid

SAFE_IDS = {0, 32, 55, 56, 57}  # IDs considered safe to teleport onto

class Tunnel(Cell):
    found_tunnel_once = False  # track discovery

    def __init__(self):
        super().__init__()
        self.grid: Optional[CellGrid] = None
        self.col(15, 7)
        self.load_dos_char(239)

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            if not self.grid:
                return False

            px_old, py_old = cell.x, cell.y

            # Get all tunnels from the grid
            all_tunnels = [(x, y) for y in range(self.grid.rows) for x in range(self.grid.cols)
                           if isinstance(self.grid.at((x, y)), Tunnel)]

            if len(all_tunnels) < 2:
                return False  # No other tunnel to teleport to

            # Pick a random tunnel that's not the current one
            possible_destinations = [(x, y) for (x, y) in all_tunnels if (x, y) != (px_old, py_old)]
            dest_x, dest_y = random.choice(possible_destinations)

            # Try placing player directly to the right first, then other directions
            offsets = [(1, 0), (0, -1), (0, 1), (-1, 0)]  # right, up, down, left
            found_spot = False

            for dx, dy in offsets:
                new_x = dest_x + dx
                new_y = dest_y + dy

                if 0 <= new_x < self.grid.cols and 0 <= new_y < self.grid.rows:
                    target = self.grid.at((new_x, new_y))
                    if target is None or (hasattr(target, "id") and target.id in SAFE_IDS):
                        dest_x, dest_y = new_x, new_y
                        found_spot = True
                        break

            if not found_spot:
                # If can't find immediately nearby, try random nearby tiles
                for _ in range(100):
                    offset_x = random.randint(-1, 1)
                    offset_y = random.randint(-1, 1)
                    new_x = dest_x + offset_x
                    new_y = dest_y + offset_y

                    if not (0 <= new_x < self.grid.cols and 0 <= new_y < self.grid.rows):
                        continue

                    target = self.grid.at((new_x, new_y))
                    if target is None or (hasattr(target, "id") and target.id in SAFE_IDS):
                        dest_x, dest_y = new_x, new_y
                        found_spot = True
                        break

            if not found_spot:
                # Total fallback: stay at old position
                dest_x, dest_y = px_old, py_old

            # Move the player forcibly to new position
            self.grid.move_to((dest_x, dest_y), cell)

            if not Tunnel.found_tunnel_once:
                print("You passed through a secret Tunnel!")
                Tunnel.found_tunnel_once = True

            return False

        return False
