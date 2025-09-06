import pygame
import random
import os
pygame.mixer.init()
pygame.init()

# --- Screen setup ---
screen_width = 900
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game - Complete Version")

# --- Colors ---
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 200, 0)
blue = (50, 150, 255)

# --- Clock & Font ---
fps = 30
clock = pygame.time.Clock(fps)
font = pygame.font.SysFont(None, 45)

# --- Highscore file setup ---
if not os.path.exists(r"../docs/Snake_High_Score.txt"):
    with open("highscore.txt", "w") as f:
        f.write("0")

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(blue)
        text_screen("Welcome to Snake Game!", white, 220, 200)
        text_screen("Press SPACE to Play", white, 250, 260)
        text_screen("Press Q to Quit", white, 290, 320)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                elif event.key == pygame.K_q:
                    exit_game = True

def gameloop():
    # --- Game variables ---
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 20
    snake_list = []
    snake_length = 1

    # Food (fixed randint issue)
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)

    score = 0
    init_velocity = 5
    game_over = False
    exit_game = False

    with open("highscore.txt", "r") as f:
        highscore = int(f.read())

    while not exit_game:
        if game_over:
            with open(r"../docs/Snake_High_Score.txt", "w") as f:
                f.write(str(highscore))

            game_window.fill(black)
            text_screen("Game Over! Press Enter to Restart or Q to Quit", red, 80, 250)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    elif event.key == pygame.K_q:
                        exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    elif event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Snake eats food (fixed randint issue)
            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 10
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snake_length += 5
                if score > highscore:
                    highscore = score
                # Increase speed as score grows
                init_velocity += 0.2

            game_window.fill(green)
            game_window.blit()
            text_screen(f"Score: {score}  Highscore: {highscore}", white, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(game_window, black, snake_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

    pygame.quit()
    quit()

welcome()
