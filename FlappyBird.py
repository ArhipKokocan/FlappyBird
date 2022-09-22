import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
BLUE = (1, 0, 231)
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

def draw_bird(x, y):
    bird = pygame.draw.rect(screen, 'yellow', [x, y, 30, 30], 0, 8)
    return bird

# bird variables
bird_x = 400
bird_y = 300
GREEN = (1, 223, 1)


while True:

    timer.tick(FPS)
    screen.fill(BLUE)
    bird = draw_bird(bird_x, bird_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.display.flip()
    pygame.display.update()