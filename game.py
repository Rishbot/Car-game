# Example file showing a circle moving on screen
import random
import pygame
from core import Car, EnemyCar, Map

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

car1 = Car("X", 100, 1, random.randint(100,1000), random.randint(100,600))
car2 = EnemyCar("+", 100, 1, random.randint(100,1000), random.randint(100,600))
cars = [car1, car2]
map = Map("grid", {"x": random.randint(100,1000), "y": random.randint(100,600)})



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "red", (car1.x, car1.y), 25)
    pygame.draw.circle(screen, "blue", (car2.x, car2.y), 25)
    pygame.draw.circle(screen, "green", (map.goal["x"], map.goal["y"]), 25)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        car1.forward()
    if keys[pygame.K_a]:
        car1.left()
    if keys[pygame.K_d]:
        car1.right()
    if keys[pygame.K_s]:
        car1.backward()
    
    if map.completed:
        print("You Win!")
        exit()

    if not car2.caught_player:
        if random.randint(0, 1) == 0:
            car2.move(car1)
    else:
        print("Game Over!")
        exit()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    clock.tick(60)

pygame.quit()