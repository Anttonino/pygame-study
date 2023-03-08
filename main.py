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
black = 0, 0 ,0

# Positions
x = width / 2
y = height / 2
x_obstacle = randint (40, 600)
y_obstacle = randint (50, 430)

# Score 
score = 0
font = pygame.font.SysFont('arial', 40, True, True)

# Display Config
screen = pygame.display.set_mode((size))
pygame.display.set_caption('Display Config')
clock = pygame.time.Clock()

# Primary Loop (The Game)
while True:
    # Framaskip 
    clock.tick(60)
    # Screen Color
    screen.fill((black))
    # Game Score
    message = f'Score: {score}'
    score_render = font.render(message, True, (255,255,255))
    # Secondary loop (Check events in game)
    for event in pygame.event.get ():
        # Quit Game
        if event.type == QUIT:
            pygame.quit()
            exit()
        # Input Config
        if pygame.key.get_pressed()[K_a]:
            x -= 10
        if pygame.key.get_pressed()[K_d]:
            x += 10
        if pygame.key.get_pressed()[K_w]:
            y -= 10
        if pygame.key.get_pressed()[K_s]:
            y += 10
    # Objects
    palyer = pygame.draw.rect(screen, (255,0,0), (x, y, 40,50))
    obstacle = pygame.draw.rect(screen, (0,0,255), (x_obstacle, y_obstacle, 40,50))
    # Collision between player and obstacle
    if palyer.colliderect (obstacle):
        x_obstacle = randint(40, 600)
        y_obstacle = randint(50, 430)
        score += 1
        point_effect.play()
    # Score position in screen
    screen.blit(score_render, (430,40))
    # Refresh the screen while the primary loop receives new information
    pygame.display.update ()