if __name__ == "__main__":
    import pygame
    import sys

    # Support reading SCALE passed after restart
    if len(sys.argv) >= 2:
        try:
            import constants
            constants.SCALE = float(sys.argv[-1])
            constants.recalculate_dimensions()
        except Exception:
            pass

    pygame.init()

    from game import Game
    game = Game()
    game.run()

    pygame.quit()
