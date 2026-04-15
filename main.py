import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
# or import everything: from module_name import *


# clock = pygame.time.Clock()
# dt = 0



def main():
    pygame.init()
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
        # GAME LOOP
    while True:
        log_state()
        # Events
        for event in pygame.event.get():
            pass
            

            if event.type == pygame.QUIT:
                return
        # time_passed = clock.tick(60)
        # seconds = time_passed/1000
        # dt += seconds
        # print(dt) 
        screen.fill('black')
        pygame.display.flip()
    

if __name__ == "__main__":
    main()
