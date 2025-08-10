import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion', direction: str = 'right') -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        ship = game.ship

        self.image = pygame.image.load(self.settings.bullet_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h))
        
        if direction == 'right':
            deg = getattr(self.settings, 'bullet_deg_right', -90)
            self.dx = self.settings.bullet_speed
        else:
            deg = getattr(self.settings, 'bullet_deg_left', 90)
            self.dx = -self.settings.bullet_speed

        self.image = pygame.transform.rotate(self.image, deg)
        self.rect = self.image.get_rect()

        if direction == 'right':
            self.rect.midleft = ship.rect.midright
        else:
            self.rect.midright - ship.rect.midleft
        self.rect.centery = ship.rect.centery

        self.x = float(self.rect.x)
    
    def update(self):
        self.x += self.dx
        self.rect.x = int(self.x)
        if self.rect.right < 0 or self.rect.left >self.settings.screen_w:
            self.kill()

    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)