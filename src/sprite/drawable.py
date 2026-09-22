import pygame
from typing import Protocol

class Drawable(Protocol):
    rect: pygame.Rect
    y: float
    image: pygame.Surface
    layer: int