import pygame
import sys
import random


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

def draw_block(blk, y, bird):
    global end_game
    for i in range(len(blk)):
        top_block = pygame.draw.rect(screen, 'green', [blk[i], 0, 35, y[i]])
        down_block = pygame.draw.rect(screen, 'green', [blk[i], y[i] + 210, 35, HEIGHT - (y[i] - 50)])

        if top_block.colliderect(bird) or down_block.colliderect(bird):
            end_game = True


# bird variables
bird_x = 200
bird_y = 255
new_x = 0
new_y = 0
jump = 15
gravitation = 1.5

# obstacle variables
blocks = [400, 700, 1000, 1300, 1600]
block_generator = True
y_pos = []
end_game = False
speed = 5
score = 0
high_score = 0

font = pygame.font.Font(pygame.font.get_default_font(), 36)

while True:

    timer.tick(FPS)
    screen.fill(BLUE)

    if block_generator:
        for i in range(len(blocks)):
            y_pos.append(random.randint(0, 350))
        block_generator = False

    bird = draw_bird(bird_x, bird_y, new_y)
    draw_block(blocks, y_pos, bird)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not end_game:
                new_y = -jump
            if event.key == pygame.K_SPACE and end_game:
                bird_x = 200
                bird_y = 255
                new_y = 0
                block_generator = True
                blocks = [400, 700, 1000, 1300, 1600]
                y_pos = []
                score = 0
                end_game = False


    if bird_y + new_y < HEIGHT - 30:
        bird_y += new_y
        new_y += gravitation
    else:
        bird_y = HEIGHT - 30

    for i in range(len(blocks)):
        if not end_game:
            blocks[i] -= speed
            if blocks[i] < -30:
                blocks.remove(blocks[i])
                y_pos.remove(y_pos[i])
                blocks.append(random.randint(blocks[-1] + 300, blocks[-1] + 350))
                y_pos.append(random.randint(0, 350))
                score += 1

    if score > high_score:
        high_score = score

    if end_game is True:
        game_over_text = font.render(f'Game is over! Click space to start again!', True, 'black')
        screen.blit(game_over_text, (50, 300))

    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, dest=(10, 0))
    high_score_text = font.render(f'High score: {high_score}', True, 'white')
    screen.blit(high_score_text, dest=(10, 35))
    pygame.display.flip()
    pygame.display.update()