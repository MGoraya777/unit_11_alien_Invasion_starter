import sys
import pygame

class AlienInvasion:

    def __init__(self_) -> None:
        pygame.init()

        self_.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')

        self_.running = True
    
    def run_game(self):
        # Game loop
        while self.running:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
    pass