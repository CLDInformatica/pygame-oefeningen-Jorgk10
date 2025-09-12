'''
Maak het plaatje dat in dit mapje staat na.

Slides: 
https://docs.google.com/presentation/d/1YwoUdeWABUYJkSfNzzZzDbCKvCVmWoo9Z5Uu7f_Y_K4/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Eerste game!')
clock = pygame.time.Clock()
running = True

surface = pygame.Surface((800, 400))
surface.fill("blue")


'''-------------------------- Pijp -------------------------- '''
pijp = pygame.Surface((45, 200))
pijp.fill("green")
pijp1 = pygame.Surface((45, 60))
pijp1.fill("green")
pijp2 = pygame.Surface((45, 60))
pijp2.fill("green")
pijp3 = pygame.Surface((45, 250))
pijp3.fill("green")
pijp4 = pygame.Surface((45, 250))
pijp4.fill("green")
pijp5 = pygame.Surface((45, 60))
pijp5.fill("green")


goon = pygame.Surface((30, 30))
goon.fill("yellow")

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False


  screen.blit(surface, (0, 0))
  screen.blit(goon, (50, 200)) 
  
  '''-------------------------- Pijp -------------------------- '''
  screen.blit(pijp, (200, 0)) 
  screen.blit(pijp1, (200, 340)) 
  screen.blit(pijp2, (400, 0)) 
  screen.blit(pijp3, (400, 150))   
  screen.blit(pijp4, (600, 0)) 
  screen.blit(pijp5, (600, 340))   

  pygame.display.update()
  clock.tick(60)
