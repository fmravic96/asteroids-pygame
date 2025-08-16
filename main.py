import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Clear the screen with black

        for entity in drawable:
            entity.draw(screen)

        dt = clock.tick(60) / 1000  # Cap the frame rate at 60 FPS
        updatable.update(dt)

        for obj in asteroids:
            if obj.check_collision(player):
                print("Game over!")
                sys.exit()
                
            # check if bullets collided
            for shot in shots:
                if obj.check_collision(shot):
                    print("Asteroid hit!")
                    new_asteroids = obj.split()
                    if new_asteroids:
                        for new_asteroid in new_asteroids:
                            asteroids.add(new_asteroid)
                    shot.kill()
                    break

        pygame.display.flip()  # Update the display

if __name__ == "__main__":
    main()
