import pygame
from src.entities.drawable import Drawable


class StaticBody(Drawable):
    def __init__(
            self,
            midbottom: pygame.Vector2 | tuple[float, float],
            collider_size: tuple[int, int],
        ):

        self.collider = pygame.FRect((0, 0), collider_size)
        self.collider.midbottom = midbottom
        self.z

    @property
    def centery(self) -> float:
        return self.collider.centery
