import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self_) -> None:
        pygame.init()
        self_.settings = Settings()

        self_.screen = pygame.display.set_mode(
            (self_.settings.screen_w, self_.settings.screen_h))
        pygame.display.set_caption('Alien Invasion')

        self_.bg = pygame.image.load(self_.settings.bg_file)
        self_.bg = pygame.transform.scale(
            self_.bg,
            (self_.settings.screen_w, self_.settings.screen_h))

        self_.running = True
        self_.clock = pygame.time.Clock()

        self_.ship = Ship(self_)
    
    def run_game(self):
        # Game loop
        while self.running:
            self._check_events()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
    pass