import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
BLUE = (1, 0, 231)
FPS = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
pygame.display.set_caption('FlappyBird')

def draw_bird(x, y, new_y):

    mouth = pygame.draw.circle(screen, (211, 156, 1), [x + 30, y + 15], 12)
    bird = pygame.draw.rect(screen, 'yellow', [x, y, 30, 30], 0, 8)
    eye = pygame.draw.circle(screen, 'black', [x + 20, y + 10], 5)

    # drawing boost lines
    if new_y < 0:
        boost_red1 = pygame.draw.rect(screen, 'red', [x + 20, y + 35, 7, 25], 0, 2)
        boost_red2 = pygame.draw.rect(screen, 'red', [x + 5, y + 35, 7, 25], 0, 2)
    return bird


# bird variables
bird_x = 200
bird_y = 255
new_x = 0
new_y = 0
jump = 15
gravitation = 1.5


while True:

    timer.tick(FPS)
    screen.fill(BLUE)
    bird = draw_bird(bird_x, bird_y, new_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_y = -jump

    if bird_y + new_y < HEIGHT - 30:
        bird_y += new_y
        new_y += gravitation
    else:
        bird_y = HEIGHT - 30



    pygame.display.flip()
    pygame.display.update()