from enum import Enum


class GameState(Enum):
    """All of the possible game states. The values here don't really matter, and should only be referenced by State.TITLE instead of by their value directly"""

    QUIT = "QUIT"
    TITLE = "TITLE"
    GAME = "GAME"
