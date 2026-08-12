import pygame, random

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape

from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        self.x = x
        self.y = y
        self.radius = radius

        super().__init__(x, y, radius)



    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        #while True:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            #for i in range(2):
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            first_angle = self.velocity.rotate(new_angle)
            second_angle = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS



            mini_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            print("Created new Asteroid One")
            mini_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            print("Created new Asteroid Two")

            mini_asteroid_one.velocity = first_angle * 1.2
            mini_asteroid_two.velocity = second_angle * 1.2
