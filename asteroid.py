import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, image=None):
        super().__init__(x, y, radius)
        self.image = image
    
    def draw(self, screen):
        if self.image:
            # Scale the image based on the asteroid's radius
            scaled_image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
            
            # Calculate the top-left position to center the image
            top_left_position = (self.position.x - self.radius, self.position.y - self.radius)
            
            # Draw the scaled image
            screen.blit(scaled_image, top_left_position)

            # Draw wrapped images for asteroids appearing on screen edges
            for offset in CircleShape.offsets:
                wrapped_position = pygame.Vector2(self.position) + pygame.Vector2(offset) - pygame.Vector2(self.radius, self.radius)
                screen.blit(scaled_image, wrapped_position)
        else:
            # Draw a circle if no image is provided
            pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

            for offset in CircleShape.offsets:
                wrapped_position = (self.position.x, self.position.y) + pygame.Vector2(offset)
                pygame.draw.circle(screen, "white", wrapped_position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap()

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