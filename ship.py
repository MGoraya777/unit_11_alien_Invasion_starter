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
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))
        
        self.rect = self.image.get_rect()

        side = getattr(self.settings, 'ship_side', 'left')

        if side == 'left':
            self.facing = 'right'
            deg = getattr(self.settings, 'ship_deg_right', -90)
        else:
            self.facing = 'left'
            deg = getattr(self.settings, 'ship_deg_left', 90)

        self.image = pygame.transform.rotate(self.image, deg)
        self.rect = self.image.get_rect()

        if side == 'left':
            self.rect.left = self.boundaries.left
        else:
            self.rect.right = self.boundaries.right

        self._center_ship()
        self.moving_up = False
        self.moving_down = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.centery = self.boundaries.centery
        self.y = float(self.rect.y)

    def update(self):
        # updating position of ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = int(self.y)

        if getattr(self.settings, 'ship_side', 'left') == 'left':
            self.rect.left = self.boundaries.left
        else:
            self.rect.right = self.boundaries.right

    def draw(self) -> None:
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        return self.arsenal.fire_bullet(direction = self.facing)
    
    def check_collisions(self, other_group) -> bool:
        if pygame.sprite.spritecollideany(self, other_group):
            if getattr(self.settings, 'ship_side', 'left') == 'left':
                self.rect.left = self.boundaries.left
            else:
                self.rect.right = self.boundaries.right
            self.rect.centery = self.boundaries.centery
            self.y = float(self.rect.y)
            return True
        return False  
