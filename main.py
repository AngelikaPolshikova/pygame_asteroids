import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from asteroid import *
from asteroidfield import AsteroidField
from logger import log_event 
from circleshape import *
import sys
from shot import *





def main():
    pygame.init()
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    
    # Group class is a container to hold & manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, drawable, updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player_object = Player(x, y)


        # GAME LOOP
    while True:
        log_state()
        # Events
        for event in pygame.event.get():
            pass
            

            if event.type == pygame.QUIT:
                return
        time_passed = clock.tick(60)
        seconds = time_passed/1000
        dt = seconds
         
        screen.fill('black')
        updatable.update(dt)
        for i in drawable:
            i.draw(screen)
        
        for a in asteroids: #a - each asteroid
            if a.collides_with(player_object):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # each shot and each asteroid gets destroyed   
            for s in shots: #s-each shot 
                if s.collides_with(a):
                    log_event("asteroid_shot")
                    s.kill() 
                    a.split()
        
       
        
        
        pygame.display.flip()
    

if __name__ == "__main__":
    main()

