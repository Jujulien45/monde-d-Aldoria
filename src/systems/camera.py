import pygame
from src.entities.drawable import Drawable

class Camera:
    def __init__(self, screen_surface: pygame.Surface):
        self.offset = pygame.Vector2(0.0, 0.0)
        self.screen_surface: pygame.Surface = screen_surface
        self.size: tuple[int, int] = screen_surface.get_size()

    def set_target(self, target_pos: pygame.Vector2):
        self.offset = target_pos - pygame.Vector2(self.size) / 2

    def world_to_screen(self, position: pygame.Vector2 | tuple[int, int]):
        return  - self.offset + position

    def screen_to_world(self, position: pygame.Vector2 | tuple[int, int]):
        return self.offset + position

    def draw(self, drawables: list[Drawable]):
        ordered_drawables: list[Drawable] = sorted(drawables, key = lambda dwbl: (dwbl.y, dwbl.layer))

        for drawable in ordered_drawables:
            screen_pos = self.world_to_screen(drawable.rect.topleft)
            self.screen_surface.blit(drawable.image, screen_pos)