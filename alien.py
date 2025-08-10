import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import Alienfleet

class Alien(Sprite):
    def __init__(self, fleet: 'Alienfleet', x: float, y: float) -> None:
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self) -> None:
       self.y += self.fleet.fleet_direction * self.fleet.game.settings.fleet_speed
       self.rect.x = int(self.x)
       self.rect.y = int(self.y)

    def check_edges(self):
        return (self.rect.top  <= 0 or self.rect.bottom >= self.boundaries.bottom)
                
    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)