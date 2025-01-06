import pygame
from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SHOT_LIFETIME, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.kill_timer = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

        # Draw the shot in all wrapped positions
        for offset in CircleShape.offsets:
            wrapped_position = (self.position.x, self.position.y) + pygame.Vector2(offset)
            pygame.draw.circle(screen, "white", wrapped_position, self.radius, 2)

    def update(self, dt):
        self.kill_timer += dt
        if self.kill_timer > SHOT_LIFETIME:
            self.kill()
        self.position += self.velocity * dt

        self.wrap()