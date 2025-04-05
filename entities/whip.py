from constants import WHITE
from entities.player import Player
from renderer.cell import Cell

class Whip(Cell):
    def __init__(self) -> None:
        super().__init__()
        self.col(15, 7)
        self.load_dos_char(244)
        
    def use_whip(self):
        if self.whip_count > 0:
            self.whip_count -= 1
            #whip_sound.play() 
            return True
        return False

    def on_collision(self, cell: "Cell") -> bool:
        if isinstance(cell, Player):
            print("Im indiana jonesing it!!!!!")
            #if self.whip_count > 0:
                #self.whip_count -= 1
                #whip_sound.play() 
                #eturn True
            #return False
            #from level.level_load import game_instance
            #if game_instance:
                #game_instance.whip_count += 1
            return True
        return False
    
    '''def activate(self):
        if self.player.use_whip():
            hits = []
            if self.player.y > 100 and self.player.x > 100:
                hits.append((self.player.x - 1, self.player.y - 1, '\\'))
            if self.player.x > 100:
                hits.append((self.player.x - 1, self.player.y, 'ƒ'))
            if self.player.y < 500 and self.player.x > 100:
                hits.append((self.player.x - 1, self.player.y + 1, '/'))
            if self.player.y < 500:
                hits.append((self.player.x, self.player.y + 1, '≥'))
            if self.player.y < 500 and self.player.x < 700:
                hits.append((self.player.x + 1, self.player.y + 1, '\\'))
            if self.player.x < 700:
                hits.append((self.player.x + 1, self.player.y, 'ƒ'))
            if self.player.y > 100 and self.player.x < 700:
                hits.append((self.player.x + 1, self.player.y - 1, '/'))
            if self.player.y > 100:
                hits.append((self.player.x, self.player.y - 1, '≥'))'''
                # Need to implement pressing w 

    #TODO: get player count of whips
        #button to use whip
        #in use whip function, have whip spin around
        #if whip hits enemy, it dies
        #if whip hits wall, chance for wall to break

