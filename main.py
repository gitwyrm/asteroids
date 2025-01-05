import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from test.profilee import C

from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    while True:
        # Quit if window closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # paint screen black
        screen.fill(color=(0, 0, 0))

        for entity in updatable:
            entity.update(dt)

        for entity in asteroids:
            if entity.collision_with(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if entity.collision_with(shot):
                    entity.kill()
                    shot.kill()

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
