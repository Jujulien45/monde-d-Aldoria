import pygame
from src.objects.drawable import Drawable

class Camera:
    def __init__(self, screen_surface: pygame.Surface):
        self.offset = pygame.Vector2(0.0, 0.0)
        self.screen_surface: pygame.Surface = screen_surface
        self.size: tuple[int, int] = screen_surface.get_size()

    def set_target(self, target_pos: pygame.Vector2):
        self.offset = target_pos - pygame.Vector2(self.size) / 2

    def world_to_screen(self, position: pygame.Vector2):
        return position - self.offset

    def screen_to_world(self, position: pygame.Vector2):
        return position + self.offset

    def draw(self, objects: list[Drawable]):
        ordered_objects: list[Drawable] = sorted(objects, key = lambda obj: obj.centery)

        for obj in ordered_objects:
            offset_pos = -self.offset + obj.rect.topleft
            self.screen_surface.blit(obj.image, offset_pos)