import pygame
from constants import SCREEN_WIDTH 
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroidfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = clock.tick(60)/1000
        updatable.update(dt)
        for chestie in drawable:
            chestie.draw(screen)
        for chestie in asteroids:
            if chestie.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for glont in shots:
                if chestie.collides_with(glont):
                    log_event("asteroid_shot")
                    chestie.split()
                    glont.kill()
        pygame.display.flip()
        



if __name__ == "__main__":
    main()
