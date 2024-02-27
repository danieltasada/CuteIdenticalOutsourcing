
#library's
import sys

import pygame
from pygame.locals import QUIT

#variables
colorPlayer = (255, 0, 0)

pygame.image.load("player_sprite.png")

screen = pygame.display.set_mode(self.screen_size)


#functions


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 400))
screen.blit( img, (0, 0),)


while True: 
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        print("Left")
       
      if event.key == pygame.K_RIGHT:
        print("Right")
     
      if event.key == pygame.K_UP:
        print("Up")
       
      if event.key == pygame.K_DOWN:
        print("Down")
       
    elif event.type == QUIT:
        pygame.quit()
        sys.exit()
pygame.display.update()
pygame.display.flip()