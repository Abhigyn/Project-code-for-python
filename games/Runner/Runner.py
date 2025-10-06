import pygame
from sys import exit

pygame.init()
Screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
CLOCK = pygame.time.Clock()

Sky_surface = pygame.image.load("a/graphics/sky.png").convert()
Ground_surface = pygame.image.load("a/graphics/ground.png").convert()
snail_surface1 = pygame.image.load("a/graphics/snail/snail1.png").convert_alpha()
snail_surface2 = pygame.image.load("a/graphics/snail/snail2.png").convert_alpha()


fount1_Fonts= pygame.font.Font(r"a\font\Pixeltype.ttf",50)
text_surface = fount1_Fonts.render("My Runner",False,"Red")



snail_x_pos = 600

while True:
    snail_x_pos -= 4
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if snail_x_pos < -100: snail_x_pos = 800



    Screen.blit(Sky_surface,(0,0))
    Screen.blit(Ground_surface,(0,300))
    Screen.blit(text_surface,(300,50))
    Screen.blit(snail_surface1,(snail_x_pos,250))

    pygame.display.update()
    CLOCK.tick(60)