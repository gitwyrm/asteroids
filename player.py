import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, image=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = pygame.Vector2(0, 0)
        self.shoot_cooldown = 0
        self.image = image

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
        if self.image:
            rotated_image = pygame.transform.rotate(self.image, -self.rotation)
            rotated_rect = rotated_image.get_rect(center=self.position)
            screen.blit(rotated_image, rotated_rect)
        else:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)

        # Draw the ship in all wrapped positions
        for offset in CircleShape.offsets:
            if self.image:
                wrapped_position = (self.position.x, self.position.y) + pygame.Vector2(offset)
                rotated_image = pygame.transform.rotate(self.image, -self.rotation)
                rotated_rect = rotated_image.get_rect(center=wrapped_position)
                screen.blit(rotated_image, rotated_rect)
            else:
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

        self.wrap()

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