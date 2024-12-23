"""
I'll try to simulate movement of a galaxi. F

First i'll implement the Newton gravitation law

For gestion of acceleration, speed, position I'll use a simple aproximation, at eatch dt (here a frame of the simulation),
position += speed, speed += acceleration and acceleration = (sigma(F) /m)
"""

# Example file showing a basic pygame "game loop"
import pygame
from universe import Universe
from object import Object

sun = Object(1.9891*(10**30), [0, 0], [0, 0])
heart = Object(5.972*(10**24), [149597870700, 0], [0, 30000])

universe = Universe([sun, heart])


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screen.fill("black")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame


    # RENDER YOUR GAME HERE

    universe.evolution()

    pygame.draw.circle(screen, "blue", (heart.position[0]/149597870 + 100, heart.position[1]/149597870 + 100), 10)
    pygame.draw.circle(screen, "red", (sun.position[0]/149597870 + 100, sun.position[1]/149597870 + 100), 10)
    print("heart pos : ", (heart.position[0]/149597870 + 100, heart.position[1]/149597870 + 100))
    print("heart speed : ", heart.speed)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()