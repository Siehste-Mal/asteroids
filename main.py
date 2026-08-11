import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from logger import log_state

def main():
    clock = pygame.time.Clock()
    dt: float = 0.0

    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #size of player




    #Continuous GameLoop
    while True:
        log_state()

        #Quit Game/Window with X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Black background
        screen.fill("black")

        #Draw player on screen
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(f"{dt}")




if __name__ == "__main__":
    main()
