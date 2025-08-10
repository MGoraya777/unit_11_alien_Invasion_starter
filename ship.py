from email.mime import image
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        self.game = game
        self.settings = game.settings 
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file).convert_alpha()
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))
        
        self.side = self.settings.ship_side
        if self.side == 'right':
            self.image = pygame.transform.flip(self.img, True, False)
         
        self.rect = self.image.get_rect()

        if self.side == 'left':
            self.rect.left = self.settings.ship_border_offset
            self.fire_dir = +1
        else:
            self.rect.right = self.boundaries.right - self.settings.ship_border_offset
            self.fire_dir = -1

        self.rect.centery = self.boundaries.centery
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False
        
        self.arsenal = arsenal

    def update(self):
        # updating position of ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= temp_speed

        self.rect.y = int(self.y)
        
        if self.side == 'left':
            self.rect.left = self.settings.ship_border_offset
        else:
            self.rect.right = self.boundaries.right - self.settings.ship_border_offset

    def draw(self) -> None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        return self.arsenal.fire_bullet(self)
    
    def muzzle_pos(self):
        if self.fire_dir > 0:
            return (self.rect.right, self.rect.centery)
        else:
            return (self.rect.left, self.rect.centery)