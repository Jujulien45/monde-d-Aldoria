import pygame


class Object:
    def __init__(self):
        self.rect: pygame.Rect
        self.position: pygame.Vector2


class Camera:
    def __init__(self, screen_surface: pygame.Surface):
        self.offset = pygame.Vector2(0.0, 0.0)
        self.screen_surface: pygame.Surface = screen_surface
        self.size: tuple[int, int] = screen_surface.get_size()

    def set_target(self, target_pos: pygame.Vector2):
        self.offset = target_pos - self.size

    def world_to_screen(self, position: pygame.Vector2):
        return position - self.offset

    def screen_to_world(self, position: pygame.Vector2):
        return position + self.offset

    def draw(self, objects: list[]):

        ordered_objects: list[pygame.sprite.Sprite] = sorted(objects, key = lambda object: object.)