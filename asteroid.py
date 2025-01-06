import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, image=None):
        super().__init__(x, y, radius)
        self.image = image
        self.angle = random.uniform(0, 360)
        self.rotation_speed = random.uniform(0.1, 1.0)

    def draw(self, screen):
        if self.image:
            # Scale the image
            scaled_image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
            
            # Rotate the scaled image based on the current angle
            rotated_image = pygame.transform.rotate(scaled_image, self.angle)
            
            # Get the new rect to center the rotated image
            rect = rotated_image.get_rect(center=(self.position.x, self.position.y))

            # Draw the rotated image
            screen.blit(rotated_image, rect.topleft)

            # Draw wrapped images for asteroids appearing on screen edges
            for offset in CircleShape.offsets:
                wrapped_rect = rect.move(offset[0], offset[1])
                screen.blit(rotated_image, wrapped_rect.topleft)
        else:
            # Draw a circle if no image is provided
            pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
            for offset in CircleShape.offsets:
                wrapped_position = (self.position.x, self.position.y) + pygame.Vector2(offset)
                pygame.draw.circle(screen, "white", wrapped_position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap()
        self.angle += self.rotation_speed  # Rotate the asteroid slowly

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius, image=self.image)
        a2 = Asteroid(self.position.x, self.position.y, new_radius, image=self.image)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2