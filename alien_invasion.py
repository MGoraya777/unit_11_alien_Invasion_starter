import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

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

        self_.ship = Ship(self_, Arsenal(self_))

        pygame.mixer.init()
        self_.laser_sound = pygame.mixer.Sound(self_.settings.laser_sound)
        self_.laser_sound.set_volume(0.7)
    
    def run_game(self):
        # Game loop
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
                
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()  

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
    pass