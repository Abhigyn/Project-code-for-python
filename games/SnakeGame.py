import pygame
import random
pygame.init()


screen_width = 900
screen_height = 600
pygame.display.set_caption("SnakeGame")
pygame.display.update()
exit_game = False
game_over = False
game_window = pygame.display.set_mode((screen_width,screen_height))
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
snake_x = 45
snake_y = 55
snake_size = 10
food_x = random.randint(0,screen_width)
food_y = random.randint(0,screen_height)
snake_volicity_x = 0
snake_volicity_y = 0
clock = pygame.time.Clock()
fps = 60





pygame.draw.rect(game_window,red[food_x,food_y,snake_size,snake_size])


while not exit_game:
    for event in pygame.event():
        if event.type == pygame.QUIT:
            exit_game = True
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_RIGHT:
            snake_volicity_x = + 10
            snake_volicity_y = 0
        if event.type == pygame.K_DOWN:
            snake_volicity_y = - 10
            snake_volicity_x = 0
        if event.type == pygame.K_UP:
            snake_volicity_y = + 10
            snake_volicity_x = 0
        if event.type == pygame.K_LEFT:
            snake_volicity_x = - 10
            snake_volicity_y = 0







    snake_volicity_x = snake_x + snake_volicity_x
    snake_volicity_y = snake_y + snake_volicity_y
    game_window.fill(white)
    pygame.draw.rect(game_window,black[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()    