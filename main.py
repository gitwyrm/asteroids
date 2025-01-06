import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from button import Button
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
    button_font = pygame.font.Font(None, 40)
    game_over_font = pygame.font.Font(None, 80)
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

    restart_button = Button("Restart", SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, 150, 50, "gray", "white", button_font)
    quit_button = Button("Quit", SCREEN_WIDTH * 3 // 4 - 150, SCREEN_HEIGHT // 2, 150, 50, "gray", "white", button_font)

    paused = False

    while True:
        for event in pygame.event.get():
            # Quit if window closed
            if event.type == pygame.QUIT:
                return
            
            # handle button clicks in pause menu
            if paused:
                if restart_button.is_clicked(event):
                    print("Restarting game...")
                    player.reset()

                    for asteroid in asteroids:
                        asteroid.kill()

                    for shot in shots:
                        shot.kill()

                    asteroid_field.reset()
                    paused = False
                if quit_button.is_clicked(event):
                    print("Quitting game...")
                    pygame.quit()
                    sys.exit()

        # paint screen black
        screen.fill(color=(0, 0, 0))

        if not paused:
            for entity in updatable:
                entity.update(dt)
            
            if len(asteroids) == 0:
                paused = True

        for entity in asteroids:
            if entity.collision_with(player):
                paused = True
            
            for shot in shots:
                if entity.collision_with(shot):
                    entity.split()
                    shot.kill()

        for entity in drawable:
            entity.draw(screen)

        if paused:
            if(len(asteroids) == 0):
                game_over_text = game_over_font.render("YOU WIN", True, "green")
            else:
                game_over_text = game_over_font.render("GAME OVER", True, "red")
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
            screen.blit(game_over_text, text_rect)
            restart_button.draw(screen)
            quit_button.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
