import pygame
import random
import os
import sys

pygame.init()
pygame.mixer.init()

# ----------------- Screen Setup -----------------
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with Sprites")

clock = pygame.time.Clock()
fps = 10   # snake moves in steps, so 10 FPS is smooth enough

# ----------------- Paths -----------------
base_path = os.path.dirname(__file__)
graphics_path = os.path.join(base_path, "snake_graphics")
audio_path = os.path.join(base_path, "Snake_audio")

# ----------------- Load Helpers -----------------
def load_and_scale(path, size):
    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, size)
    except pygame.error as e:
        print(f"Error loading image at {path}: {e}")
        return pygame.Surface(size, pygame.SRCALPHA)

def load_sound(path):
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    return None

# ----------------- Load Assets -----------------
apple_img = load_and_scale(os.path.join(graphics_path, "apple.png"), (30, 30))
head_up_img = load_and_scale(os.path.join(graphics_path, "head_up.png"), (30, 30))
head_down_img = load_and_scale(os.path.join(graphics_path, "head_down.png"), (30, 30))
head_right_img = load_and_scale(os.path.join(graphics_path, "head_right.png"), (30, 30))
head_left_img = load_and_scale(os.path.join(graphics_path, "head_left.png"), (30, 30))
body_img = load_and_scale(os.path.join(graphics_path, "body_horizontal.png"), (30, 30))

intro_img = load_and_scale(os.path.join(graphics_path, "Intro.png"), (screen_width, screen_height))
outro_img = load_and_scale(os.path.join(graphics_path, "Outro.png"), (screen_width, screen_height))

bg1_img = load_and_scale(os.path.join(graphics_path, "bg.png"), (screen_width, screen_height))
bg2_img = load_and_scale(os.path.join(graphics_path, "bg2.png"), (screen_width, screen_height))

bg_music = os.path.join(audio_path, "Baground.wav")
eat_sound = load_sound(os.path.join(audio_path, "Beep.wav"))
go_sound = load_sound(os.path.join(audio_path, "GameOver.wav"))

# ----------------- Colors -----------------
COLOR_MAP = {
    "Blue": (0, 128, 255),
    "Green": (0, 200, 0),
    "White": (255, 255, 255),
    "Black": (0, 0, 0)
}

# ----------------- Global Settings -----------------
current_snake_color = "Blue"
current_bg = "bg1"

# ----------------- Sprite Tinting -----------------
def tint_image(image, color):
    tinted = image.copy()
    tint_surf = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    tint_surf.fill(color + (255,))  # full alpha to apply color
    tinted.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted

def apply_snake_color(color_name):
    global head_up_img, head_down_img, head_left_img, head_right_img, body_img
    color = COLOR_MAP[color_name]

    # reload original images
    up = load_and_scale(os.path.join(graphics_path, "head_up.png"), (30, 30))
    down = load_and_scale(os.path.join(graphics_path, "head_down.png"), (30, 30))
    left = load_and_scale(os.path.join(graphics_path, "head_left.png"), (30, 30))
    right = load_and_scale(os.path.join(graphics_path, "head_right.png"), (30, 30))
    body = load_and_scale(os.path.join(graphics_path, "body_horizontal.png"), (30, 30))

    # tint
    head_up_img = tint_image(up, color)
    head_down_img = tint_image(down, color)
    head_left_img = tint_image(left, color)
    head_right_img = tint_image(right, color)
    body_img = tint_image(body, color)

apply_snake_color(current_snake_color)

# ----------------- Snake Drawing -----------------
def draw_snake(snake_list, direction):
    if not snake_list:
        return
    
    # draw body if length > 1
    for block in snake_list[:-1]:
        screen.blit(body_img, (block[0], block[1]))

    # always draw head
    head = snake_list[-1]
    if direction == "up":
        screen.blit(head_up_img, head)
    elif direction == "down":
        screen.blit(head_down_img, head)
    elif direction == "left":
        screen.blit(head_left_img, head)
    elif direction == "right":
        screen.blit(head_right_img, head)


# ----------------- Menu Helpers -----------------
font = pygame.font.SysFont(None, 48)

def draw_text(text, pos, selected=False):
    color = (255, 255, 0) if selected else (255, 255, 255)
    render = font.render(text, True, color)
    rect = render.get_rect(center=pos)
    screen.blit(render, rect)
    return rect

def play_music():
    if os.path.exists(bg_music):
        pygame.mixer.music.load(bg_music)
        pygame.mixer.music.play(-1)

# ----------------- Intro Menu -----------------
def intro_menu():
    play_music()
    options = ["Play", "Options", "Quit"]
    selected = 0

    while True:
        screen.blit(intro_img, (0, 0))
        rects = []
        for i, opt in enumerate(options):
            rects.append(draw_text(opt, (screen_width//2, 300 + i*60), i == selected))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected] == "Play":
                        return "play"
                    elif options[selected] == "Options":
                        return "options"
                    elif options[selected] == "Quit":
                        pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, r in enumerate(rects):
                    if r.collidepoint(event.pos):
                        if options[i] == "Play":
                            return "play"
                        elif options[i] == "Options":
                            return "options"
                        elif options[i] == "Quit":
                            pygame.quit(); sys.exit()

# ----------------- Options Menu -----------------
def options_menu():
    global current_snake_color, current_bg
    selected = 0

    while True:
        screen.fill((0,0,0))
        rects =[]
        options = [
            "Snake Color: " + current_snake_color,
            "Background: " + current_bg,
            "Back"
        ]


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if options[selected].startswith("Snake Color"):
                        # cycle color
                        colors = list(COLOR_MAP.keys())
                        idx = colors.index(current_snake_color)
                        current_snake_color = colors[(idx+1)%len(colors)]
                        apply_snake_color(current_snake_color)
                        options[0] = "Snake Color: " + current_snake_color
                    elif options[selected].startswith("Background"):
                        current_bg = "bg2" if current_bg == "bg1" else "bg1"
                        options[1] = "Background: " + current_bg
                    elif options[selected] == "Back":
                        return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, r in enumerate(rects):
                    if r.collidepoint(event.pos):
                        if options[i].startswith("Snake Color"):
                            colors = list(COLOR_MAP.keys())
                            idx = colors.index(current_snake_color)
                            current_snake_color = colors[(idx+1)%len(colors)]
                            apply_snake_color(current_snake_color)
                            options[0] = "Snake Color: " + current_snake_color
                        elif options[i].startswith("Background"):
                            current_bg = "bg2" if current_bg == "bg1" else "bg1"
                            options[1] = "Background: " + current_bg
                        elif options[i] == "Back":
                            return

# ----------------- Game Over Screen -----------------
def game_over_screen():
    pygame.mixer.music.stop()
    if go_sound: go_sound.play()
    screen.blit(outro_img, (0, 0))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# ----------------- Game Loop -----------------
def gameloop():
    snake_x, snake_y = (screen_width//2),(screen_height//2)
    x_velocity, y_velocity = 30, 0  # start moving right
    direction = "right"

    snake_list = [[snake_x, snake_y]]
    snake_length = 1

    apple_x = random.randrange(0, screen_width - 30, 30)
    apple_y = random.randrange(0, screen_height - 30, 30)

    game_over = False

    while not game_over:
        bg_img = bg1_img if current_bg == "bg1" else bg2_img


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_velocity == 0:
                    x_velocity, y_velocity, direction = -30, 0, "left"
                elif event.key == pygame.K_RIGHT and x_velocity == 0:
                    x_velocity, y_velocity, direction = 30, 0, "right"
                elif event.key == pygame.K_UP and y_velocity == 0:
                    x_velocity, y_velocity, direction = 0, -30, "up"
                elif event.key == pygame.K_DOWN and y_velocity == 0:
                    x_velocity, y_velocity, direction = 0, 30, "down"

        snake_x += x_velocity
        snake_y += y_velocity
        head = [snake_x, snake_y]
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # eating apple
        snake_rect = pygame.Rect(snake_x, snake_y, 30, 30)
        apple_rect = pygame.Rect(apple_x, apple_y, 30, 30)
        if snake_rect.colliderect(apple_rect):
            if eat_sound: eat_sound.play()
            snake_length += 1
            apple_x = random.randrange(0, screen_width // 30) * 30
            apple_y = random.randrange(0, screen_height // 30) * 30


        # wall collision
        if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
            game_over = True

        # self collision
        if head in snake_list[:-1]:
            game_over = True

        # draw
        screen.blit(bg_img, (0, 0))
        screen.blit(apple_img, (apple_x, apple_y))
        draw_snake(snake_list, direction)
        pygame.display.update()
        clock.tick(fps)

    game_over_screen()

# ----------------- Main -----------------
if __name__ == "__main__":
    while True:
        choice = intro_menu()
        if choice == "play":
            gameloop()
        elif choice == "options":
            options_menu()
