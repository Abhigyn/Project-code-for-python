import pygame
x = pygame.init()
Gamedisplay = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")





exit_game = False
game_over = False
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:



# pygame.quit()
# quit()