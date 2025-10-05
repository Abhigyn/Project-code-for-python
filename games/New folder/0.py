import pygame
from sys import exit

pygame.init()
Screen = pygame.display.set_mode((800,400))
CLOCK = pygame.time.Clock()
# test_surface =


while True:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    Screen.blit()
    pygame.display.update()
    CLOCK.tick(60)