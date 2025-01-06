import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.shoot_cooldown = 0

    def reset(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the ship normally
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

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

        # Draw the ship in all wrapped positions
        for offset in offsets:
            wrapped_position = [point + pygame.Vector2(offset) for point in self.triangle()]
            pygame.draw.polygon(screen, "white", wrapped_position, 2)

    def update(self, dt):
        self.shoot_cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.thrust(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Apply velocity to the position
        self.position += self.velocity * dt

        # Screen wrapping logic
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0

        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def thrust(self, dt):
        # Accelerate in the direction the ship is facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt

        # Cap the maximum speed
        if self.velocity.length() > PLAYER_MAX_SPEED:
            self.velocity.scale_to_length(PLAYER_MAX_SPEED)

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        vec = pygame.math.Vector2(0, 1)
        vec = vec.rotate(self.rotation)
        shot.velocity = vec * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN