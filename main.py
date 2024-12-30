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
heart = Object(-5.972*(10**24), [149597870700, 0], [-300000, 0])
heartinit = Object(0, [149597870700, 0], [0, 0])

universe = Universe([sun, heart, heartinit])



"""
graph part, I have to do it better but, it's not fun so... I'll do it later
"""

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                for object in universe.objects:
                    object.position[1] -= 1000000000
            elif event.key == pygame.K_s:
                for object in universe.objects:
                    object.position[1] += 1000000000
            elif event.key == pygame.K_q:
                for object in universe.objects:
                    object.position[0] -= 1000000000
            elif event.key == pygame.K_d:
                for object in universe.objects:
                    object.position[0] += 1000000000


    # RENDER YOUR GAME HERE

    screen.fill("black")

    universe.evolution()

    pygame.draw.circle(screen, "blue", (heart.position[0]/149597870 + 100, heart.position[1]/149597870 + 100), 2)
    pygame.draw.circle(screen, "green", (heartinit.position[0]/149597870 + 100, heartinit.position[1]/149597870 + 100), 2)

    pygame.draw.circle(screen, "red", (sun.position[0]/149597870 + 100, sun.position[1]/149597870 + 100), 10)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 60

pygame.quit()