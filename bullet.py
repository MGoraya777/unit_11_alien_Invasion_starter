import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from ship import Ship

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion', ship: 'Ship') -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.bullet_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h))
        
        self.dx = game.ship.fire_dir * self.settings.bullet_speed

        if self.settings.bullet_h > self.settings.bullet_w:
            self.image = pygame.transform.rotate(self.image, -90 if self.dx > 0 else 90)
        else:
            if self.dx < 0:
                self.image = pygame.transform.slip(self.image, True, False)

        self.rect = self.image.get_rect()

        mx, my = game.ship.muzzle_pos()
        if self.dx > 0:
            self.rect = self.image.get_rect(midleft = (mx, my))
        else:
            self.rect = self.image.get_rect(midright = (mx, my))

        self.x = float(self.rect.x)

    
    def update(self):
        self.x += self.dx
        self.rect.x = int(self.x)
        if self.rect.right < 0 or self.rect.left > self.screen_rect.right:
            self.kill()

    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)