'''
Gegeven is een weg en een auto. Van de auto is al een rectangle gemaakt en deze gebruiken we om de auto te plaatsen en te laten bewegen.

Van de weg is echter nog geen rectangle gemaakt.

Doe het volgende:

  - Maak een rectangle van de weg met surface.get_rect()
  - Zorg dat de center van deze rectangle in het midden van de game staat (weg precies in het midden)
  - Zorg dat de onderkant van de auto (bottom) op dezelfde plek staat als de onderkant van de weg (dan rijdt de auto namelijk op de weg)
  - Zorg dat wanneer de auto en het obstakel colliden je de auto weer naar het begin van het scherm verplaatst (de pion staat pas op de goede plek als de weg is verplaatst)

Vergeet niet om de weg_surface naar de weg_rect te blitten in plaats van naar een aantal coordinaten!

EXTRA:

Blit een stukje tekst "Game over" naar het scherm als de auto de pion raakt.

Slides: https://docs.google.com/presentation/d/1VjYiTjIcSU_x6R_K0pPASkzf7xis3oa_IpjzcmC-Wq8/edit?usp=sharing
'''
import os
import pygame

os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background_surface = pygame.Surface((800, 400))
background_surface.fill("Dark Green")

weg_surface = pygame.image.load("Opdrachten/PyGame/Les4/graphics/weg.png").convert()
weg_rect = weg_surface.get_rect(center=(399, 200))

auto_surface = pygame.image.load("Opdrachten/PyGame/Les4/graphics/auto.png").convert_alpha()
auto_rect = auto_surface.get_rect(bottom=weg_rect.bottom - 10)

obstakel_surface = pygame.image.load("Opdrachten/PyGame/Les4/graphics/obstakel.png").convert_alpha()
obstakel_rect = obstakel_surface.get_rect(bottomleft=(625, 280))

Explosion = pygame.image.load("Opdrachten/PyGame/Les4/graphics/download.png").convert_alpha()

font = pygame.font.Font(None, 74)

auto_beweegt = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_surface, (0, 0))
    screen.blit(weg_surface, weg_rect)

    if auto_beweegt:
        auto_rect.left += 2
        if auto_rect.left > 800:
            auto_rect.right = 0
            screen.blit(auto_surface, auto_rect)

    if auto_rect.colliderect(obstakel_rect):
        auto_beweegt = False
        screen.blit(Explosion, (480, 135))
    else:
        screen.blit(auto_surface, auto_rect)

    
    screen.blit(obstakel_surface, obstakel_rect)

    if not auto_beweegt:
        screen.blit(auto_surface, auto_rect)

    pygame.display.update()
    clock.tick(60)
