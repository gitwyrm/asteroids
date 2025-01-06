import os
import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self, assets_path):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawned = 0
        self.assets_path = assets_path

    def spawn(self, radius, position, velocity):
        if self.spawned >= MAX_ASTEROIDS:
            return
        if USE_IMAGES:
            asteroid = Asteroid(position.x, position.y, radius, pygame.image.load(os.path.join(self.assets_path, 'asteroid.png')))
        else:
            asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity
        self.spawned += 1

    def update(self, dt):
        # spawn a new asteroid at a random edge
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, ASTEROID_KINDS)
        self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

    def reset(self):
        # Reset the spawn timer
        self.spawn_timer = 0.0
        self.spawned = 0
        