# Library
import pygame
from pygame.locals import * 
from sys import exit
from random import randint

# Library Initialization
pygame.init ()

# Music and soud effect config
pygame.mixer.music.set_volume(0.1)
background_music = pygame.mixer.music.load ('assets/background music.mp3')
pygame.mixer_music.play (-1)

point_effect = pygame.mixer.Sound('assets/point.wav')

# Display Size
size = width, height = 640, 480
white = 255, 255, 255

# Positions
x_snake = width / 2
y_snake = height / 2
x_apple = randint (40, 600)
y_apple = randint (50, 430)

# Score 
score = 0
font = pygame.font.SysFont('arial', 40, True, True)

# Display Config
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Display Config')
clock = pygame.time.Clock()

snake_length = []
def growth (snake_length):
    for XY in snake_length:
        pygame.draw.rect(screen, (0,255,0), (XY[0], XY[1], 20, 20))

# Primary Loop (The Game)
while True:
    # Framaskip 
    clock.tick(60)
    # Screen Color
    screen.fill((white))
    # Game Score
    message = f'Score: {score}'
    score_render = font.render(message, True, (0,0,0))
    # Secondary loop (Check events in game)
    for event in pygame.event.get ():
        # Quit Game
        if event.type == QUIT:
            pygame.quit()
            exit()
        # Input Config
        if pygame.key.get_pressed()[K_a]:
            x_snake -= 5
        if pygame.key.get_pressed()[K_d]:
            x_snake += 5
        if pygame.key.get_pressed()[K_w]:
            y_snake -= 5
        if pygame.key.get_pressed()[K_s]:
            y_snake += 5
    # Objects
    snake = pygame.draw.rect(screen, (0,255,0), (x_snake, y_snake, 20,20))
    apple = pygame.draw.rect(screen, (255,0,0), (x_apple, y_apple, 20,20))
    # Collision between player and obstacle
    if snake.colliderect (apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        score += 1
        point_effect.play()

    head_length = []
    head_length.append(x_snake)
    head_length.append(y_snake)
    snake_length.append(head_length)

    growth (snake_length)

    # Score position in screen
    screen.blit(score_render, (430,40))
    # Refresh the screen while the primary loop receives new information
    pygame.display.update ()