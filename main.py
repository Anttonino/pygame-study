import pygame

from pygame.locals import * 

from sys import exit

pygame.init ()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Display Config')

while True:
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit()
            exit() 
    pygame.display.update ()