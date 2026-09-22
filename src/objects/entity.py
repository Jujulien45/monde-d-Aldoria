from __future__ import annotations
from typing import TYPE_CHECKING
from src.objects.drawable import Drawable

if TYPE_CHECKING:
    from src.objects.static_body import StaticBody

import pygame


class Entity(Drawable):
    def __init__(
            self,
            midbottom: pygame.Vector2 | tuple[float, float],
            hitbox_size: tuple[int, int],
            mass: float = 1,
            collide_tiles: bool = True
    ):
        self.mass = mass
        self.collide_tiles = collide_tiles

        self.hitbox = pygame.FRect((0, 0), hitbox_size)
        self.hitbox.midbottom = midbottom
        self.velocity = pygame.Vector2(0.0, 0.0)
        self.acceleration = pygame.Vector2(0.0, 0.0)
        self._force = pygame.Vector2(0.0, 0.0)
        self.moving = False

    def apply_force(self, force: pygame.Vector2):
        self._force += force

    def solve_collision(self, delta_time: float, static_bodies: list[StaticBody]):
        # x check
        x_movement: float = self.velocity.x * delta_time

        x_projected_rect: pygame.FRect = self.hitbox.copy()
        x_projected_rect.x += self.velocity.x * delta_time


        # y check
        y_movement: float = self.velocity.y * delta_time

        y_projected_rect: pygame.FRect = self.hitbox.copy()
        y_projected_rect.y += self.velocity.y * delta_time

        # the player is also getting the self.collided_tile

        for static_body in static_bodies:
            collider = static_body.collider
            if x_projected_rect.colliderect(collider):
                # positive dir
                if self.velocity.x > 0:
                    x_contact_distance: float = collider.left - self.hitbox.right
                    x_movement = min(x_movement, x_contact_distance, key=abs)

                elif self.velocity.x < 0:
                    x_contact_distance: float = collider.right - self.hitbox.left
                    x_movement = min(x_movement, x_contact_distance, key=abs)


            if y_projected_rect.colliderect(collider):
                # positive dir
                if self.velocity.y > 0:
                    y_contact_distance: float = collider.top - self.hitbox.bottom
                    y_movement = min(y_movement, y_contact_distance, key=abs)

                elif self.velocity.y < 0:
                    y_contact_distance: float = collider.bottom - self.hitbox.top
                    y_movement = min(y_movement, y_contact_distance, key=abs)




        return x_movement, y_movement

    def update(self, delta_time: float, collision_tiles: list[StaticBody]):
        self.velocity += self._force

        # This looks weird I know, but it's acctualy the right way to do it
        self.velocity += self.acceleration * 0.5 * delta_time
        if self.collide_tiles:
            x_movement, y_movement = self.solve_collision(collision_tiles)
            self.hitbox.x += x_movement
            self.hitbox.y += y_movement
            self.moving = round(x_movement) and round(y_movement)
        else:
            self.hitbox.midbottom += self.velocity * delta_time
            self.moving = round(self.velocity.x) and round(self.velocity.y)

        self.velocity += self.acceleration * 0.5 * delta_time
        self._force.x = 0
        self._force.y = 0