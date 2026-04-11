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

car1 = Car("X", 25, 1, 2, random.randint(100,1000), random.randint(100,600))
car2 = EnemyCar("+", 25, 1, 2, random.randint(100,1000), random.randint(100,600))
car3 = EnemyCar("*", 15, 1, 2, random.randint(100,1000), random.randint(100,600))
car4 = EnemyCar("?", 40, 1, 1, random.randint(100,1000), random.randint(100,600))
cars = [car1, car2, car3, car4]
map = Map("grid", {"x": random.randint(100,1000), "y": random.randint(100,600)})
destination = pygame.Vector2(map.goal["x"], map.goal["y"])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "red", (car1.x, car1.y), car1.size)
    pygame.draw.circle(screen, "blue", (car2.x, car2.y), car2.size)
    pygame.draw.circle(screen, "yellow", (car3.x, car3.y), car3.size)
    pygame.draw.circle(screen, "purple", (car4.x, car4.y), car4.size)
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

    if not cars[1].caught_player and not cars[2].caught_player and not cars[3].caught_player:
        if random.randint(0, 1) == 0:
            car2.move(car1)
            car3.move(car1)
            car4.move(car1)
            if abs(cars[0].x - map.goal["x"]) < 35 and abs(cars[0].y - map.goal["y"]) < 35:
                map.completed = True
                print("You Win!")
                running = False
    
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