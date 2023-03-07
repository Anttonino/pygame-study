import pygame

from pygame.locals import * 

from sys import exit

pygame.init ()

width = 640
height = 480
x = width / 2
y = 0 

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
    pygame.draw.rect(screen, (255,0,0), (x, y, 40,50))
    if y >= height:
        y = 0
    y = y + 1 
    
    pygame.display.update ()