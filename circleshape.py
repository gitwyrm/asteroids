import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    # Calculate screen-wrapped positions
    offsets = [
        (SCREEN_WIDTH, 0),     # Right edge
        (-SCREEN_WIDTH, 0),    # Left edge
        (0, SCREEN_HEIGHT),    # Bottom edge
        (0, -SCREEN_HEIGHT),   # Top edge
        (SCREEN_WIDTH, SCREEN_HEIGHT),     # Bottom-right corner
        (SCREEN_WIDTH, -SCREEN_HEIGHT),    # Top-right corner
        (-SCREEN_WIDTH, SCREEN_HEIGHT),    # Bottom-left corner
        (-SCREEN_WIDTH, -SCREEN_HEIGHT),   # Top-left corner
    ]

    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def wrap(self):
         # Screen wrapping logic
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def collision_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
