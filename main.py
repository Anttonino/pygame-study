import pygame
from pygame.locals import * 
from sys import exit
from random import randint

pygame.init ()

size = width, height = 640, 480
black = 0, 0 ,0

x = width / 2
y = height / 2
x_obstacle = randint (40, 600)
y_obstacle = randint (50, 430)

score = 0
font = pygame.font.SysFont('arial', 40, True, True)

screen = pygame.display.set_mode((size))
pygame.display.set_caption('Display Config')
clock = pygame.time.Clock()

while True: 
    clock.tick(60)
    screen.fill((black))
    message = f'Score: {score}'
    score_render = font.render(message, True, (255,255,255))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if pygame.key.get_pressed()[K_a]:
            x -= 10
        if pygame.key.get_pressed()[K_d]:
            x += 10
        if pygame.key.get_pressed()[K_w]:
            y -= 10
        if pygame.key.get_pressed()[K_s]:
            y += 10

    palyer = pygame.draw.rect(screen, (255,0,0), (x, y, 40,50))
    obstacle = pygame.draw.rect(screen, (0,0,255), (x_obstacle, y_obstacle, 40,50))

    if palyer.colliderect (obstacle):
        x_obstacle = randint(40, 600)
        y_obstacle = randint(50, 430)
        score += 1
    
    screen.blit(score_render, (430,40))
    pygame.display.update ()