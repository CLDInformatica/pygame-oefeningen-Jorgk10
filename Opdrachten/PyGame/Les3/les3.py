'''
Voeg de volgende 2 dingen aan de game toe:

  - Laat de auto aan de linkerkant van het scherm terugkomen als de auto aan de rechterkant van het scherm af rijdt HINT: Gebruik een ```if``` met daarin de ```x_pos```
  - Laat een aantal regendruppels van de bovenkant van het scherm naar beneden vallen

Slides: https://docs.google.com/presentation/d/16rz2C4Pqhx4YNCokEU_5mc3rtQXXNEoi7gFAGzv9s_A/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background_surface = pygame.Surface((800, 400))
background_surface.fill("white")

auto_surface = pygame.image.load("Opdrachten/PyGame/Les3/graphics/auto.png").convert_alpha()
auto_x_pos = 200

regen = pygame.image.load("Opdrachten/PyGame/Les3/graphics/Regendruppel.png").convert_alpha()
DEFAULT_IMAGE_SIZE = (regen.get_width() // 8, regen.get_height() // 8)
regen_small = pygame.transform.scale(regen, DEFAULT_IMAGE_SIZE)
regen_y_pos = -80

regen1 = pygame.image.load("Opdrachten/PyGame/Les3/graphics/Regendruppel.png").convert_alpha()
DEFAULT_IMAGE_SIZE = (regen1.get_width() // 8, regen1.get_height() // 8)
regen1_small = pygame.transform.scale(regen1, DEFAULT_IMAGE_SIZE)
regen1_y_pos = -130

regen2 = pygame.image.load("Opdrachten/PyGame/Les3/graphics/Regendruppel.png").convert_alpha()
DEFAULT_IMAGE_SIZE = (regen2.get_width() // 8, regen2.get_height() // 8)
regen2_small = pygame.transform.scale(regen2, DEFAULT_IMAGE_SIZE)
regen2_y_pos = -200

regen3 = pygame.image.load("Opdrachten/PyGame/Les3/graphics/Regendruppel.png").convert_alpha()
DEFAULT_IMAGE_SIZE = (regen3.get_width() // 8, regen3.get_height() // 8)
regen3_small = pygame.transform.scale(regen3, DEFAULT_IMAGE_SIZE)
regen3_y_pos = -220

while running:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False

    screen.blit(background_surface, (0, 0))

    auto_x_pos += 1
    screen.blit(auto_surface, (auto_x_pos, 200))

    regen_y_pos += 1
    screen.blit(regen_small, (200, regen_y_pos))

    regen1_y_pos += 1
    screen.blit(regen1_small, (600, regen1_y_pos))
    
    regen2_y_pos += 1
    screen.blit(regen2_small, (400, regen2_y_pos))

    regen3_y_pos += 1
    screen.blit(regen3_small, (100, regen3_y_pos))

    pygame.display.update()
    clock.tick(60)

    if auto_x_pos == 800:
      auto_x_pos -= 900

    if regen_y_pos == 400:
      regen_y_pos -= 480
    
    if regen1_y_pos == 400:
      regen1_y_pos -= 530

    if regen2_y_pos == 400:
      regen2_y_pos -= 600
    
    if regen3_y_pos == 400:
      regen3_y_pos -= 620