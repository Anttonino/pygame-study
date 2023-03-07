import pygame

from pygame.locals import * 

from sys import exit

pygame.init ()

width = 640
height = 480
x = width / 2
y = height / 2

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Display Config')
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit()
            exit()
        """"
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 1
            if event.key == K_d:
                x += 1
            if event.key == K_w:
                y -= 1
            if event.key == K_s:
                y += 1
        """
        if pygame.key.get_pressed()[K_a]:
            x -= 1
        if pygame.key.get_pressed()[K_d]:
            x += 1
        if pygame.key.get_pressed()[K_w]:
            y -= 1
        if pygame.key.get_pressed()[K_s]:
            y += 1

        

    pygame.draw.rect(screen, (255,0,0), (x, y, 40,50))

    pygame.display.update ()