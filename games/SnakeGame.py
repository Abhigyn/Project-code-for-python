import pygame
import random
import os

# --- Init ---
pygame.init()
pygame.mixer.init()

# --- Screen setup ---
screen_width = 900
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game - Complete Version")

# --- Colors ---
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# --- Clock & Font ---
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45)

# --- Load images once ---
Background_image = pygame.image.load(r"../images/bg2.png").convert()
Intro_image = pygame.image.load(r"../images/Intro.png").convert()
Outro_image = pygame.image.load(r"../images/Outro1.png").convert()

# --- Load sounds once ---
bg_music = r"../audio/Baground.ogg"      # background looping music
beep_sound = pygame.mixer.Sound(r"../audio/Beep.ogg")
gameover_sound = pygame.mixer.Sound(r"../audio/GameOver.ogg")

# --- Highscore setup ---
if not os.path.exists(r"../docs/Snake_High_Score.txt"):
    with open(r"../docs/Snake_High_Score.txt", "w") as f:
        f.write("0")

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(game_window, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
#   """Intro screen"""
    pygame.mixer.music.load(bg_music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.6)

    waiting = True
    while waiting:
        game_window.blit(Intro_image, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def gameloop():
#    """Main game loop"""
    # Background music
    pygame.mixer.music.load(bg_music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.6)

    # Snake variables
    snake_x, snake_y = 45, 55
    velocity_x, velocity_y = 0, 0
    snake_size = 20
    snake_list = []
    snake_length = 1

    # Food
    food_x = random.randint(20, screen_width // 2)
    food_y = random.randint(20, screen_height // 2)

    # Game settings
    fps = 30
    score = 0
    init_velocity = 5
    game_over = False

    with open(r"../docs/Snake_High_Score.txt", "r") as f:
        highscore = int(f.read())

    while True:
        if game_over:
            with open(r"../docs/Snake_High_Score.txt", "w") as f:
                f.write(str(highscore))

            game_window.blit(Outro_image, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        return  # restart fresh
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x, velocity_y = init_velocity, 0
                    elif event.key == pygame.K_LEFT:
                        velocity_x, velocity_y = -init_velocity, 0
                    elif event.key == pygame.K_UP:
                        velocity_y, velocity_x = -init_velocity, 0
                    elif event.key == pygame.K_DOWN:
                        velocity_y, velocity_x = init_velocity, 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Snake eats food
            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                beep_sound.play()
                score += 1
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snake_length += 5
                if score > highscore:
                    highscore = score
                init_velocity += 0.2  # Increase difficulty

            # Draw everything
            game_window.blit(Background_image, (0, 0))
            text_screen(f"Score: {score}  Highscore: {highscore}", white, 5, 5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            # Collisions
            if head in snake_list[:-1] or snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                gameover_sound.play()
                game_over = True

            plot_snake(game_window, black, snake_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

# --- Run game in a controller loop ---
while True:
    welcome()
    gameloop()
