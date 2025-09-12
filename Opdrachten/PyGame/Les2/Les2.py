'''
Gegeven zijn: een horror font dat "voetbal game" op het scherm zet en een plaatje van een bal.

We gaan de game aanpassen zodat het er beter uit ziet.

Doe het volgende:

  - Download een toepasselijk font en maak hiermee een scoreboard
  - Download 2 plaatjes van voetballers en zet deze tegenover elkaar op het scherm
  - Zet de bal in het midden van de scherm

Extra tijd:

  - Voeg 2 goals toe (links en rechts)
  - Voeg een toepasselijke achtergrond toe
  - Schrijf de namen van de spelers ergens op het scherm

Slides: https://docs.google.com/presentation/d/1c4C94q8OcMGCIFefVo18Xac4WIFJacq5Eutj1gY6rCg/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Voetbal game!')
clock = pygame.time.Clock()
running = True
ScoreFont = pygame.font.Font("Opdrachten/PyGame/Les2/fonts/Montserrat-Bold.ttf", 10)

VGoal = pygame.image.load("Opdrachten/PyGame/Les2/graphics/VGoal-removebg-preview.png")
DEFAULT_IMAGE_SIZE = (VGoal.get_width() // 2, VGoal.get_height() // 2)
VGoal_small = pygame.transform.scale(VGoal, DEFAULT_IMAGE_SIZE)

voetbal_surface = pygame.image.load("Opdrachten/PyGame/Les2/graphics/grass_field.jpg")
voetbal_surface1 = pygame.image.load("Opdrachten/PyGame/Les2/graphics/voetbal.png")
DEFAULT_IMAGE_SIZE = (voetbal_surface1.get_width() // 2, voetbal_surface1.get_height() // 2)
voetbal_surface1_small = pygame.transform.scale(voetbal_surface1, DEFAULT_IMAGE_SIZE)

Klaassen = pygame.image.load("Opdrachten/PyGame/Les2/graphics/klaassen-removebg-preview.png")
DEFAULT_IMAGE_SIZE = (Klaassen.get_width() // 2, Klaassen.get_height() // 2)
Klaassen_small = pygame.transform.scale(Klaassen, DEFAULT_IMAGE_SIZE)

Ronaldo = pygame.image.load("Opdrachten/PyGame/Les2/graphics/Ronaldo-removebg-preview.png")
DEFAULT_IMAGE_SIZE = (Ronaldo.get_width() // 1.5, Ronaldo.get_height() // 1.5)
Ronaldo_small = pygame.transform.scale(Ronaldo, DEFAULT_IMAGE_SIZE)

tekst_surface = ScoreFont.render("67:00 ", False, "white")
ScoreBoard = pygame.Surface((170, 20))
ScoreBoard.fill("red")
ScoreBoard1 = pygame.Surface((30, 20))
ScoreBoard1.fill("grey")
ScoreBoard2 = pygame.Surface((30, 20))
ScoreBoard2.fill("grey")
SV_Spero = ScoreFont.render("Spe ", False, "black")
Real_Madrid = ScoreFont.render("Rma ", False, "black")
Score = ScoreFont.render("6 - 7 ", False, "white")



while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(voetbal_surface, (0, 0))
  screen.blit(ScoreBoard, (10, 10))
  screen.blit(ScoreBoard1, (50, 10))
  screen.blit(ScoreBoard2, (120, 10))
  screen.blit(tekst_surface, (14, 14))
  screen.blit(SV_Spero, (55, 14))
  screen.blit(Real_Madrid, (125, 14))
  screen.blit(Score, (89, 14))
  screen.blit(VGoal_small, (250, 25))
  screen.blit(Klaassen_small, (100, 156))
  screen.blit(Ronaldo_small, (300, 88))
  screen.blit(voetbal_surface1_small, (400, 200))
  pygame.display.update()
  clock.tick(60)