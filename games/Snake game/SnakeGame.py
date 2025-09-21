import pygame
import random
import os
import sys
import json

pygame.init()
pygame.mixer.init()

# ----------------- Screen Setup -----------------
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# ----------------- Paths -----------------
base_path = os.path.dirname(os.path.abspath(__file__))
graphics_path = os.path.join(base_path, "snake_graphics")
audio_path = os.path.join(base_path, "Snake_audio")

# <-- NEW: Set the game window icon
try:
    icon_path = os.path.join(graphics_path, "game_icon.ico") # Make sure you have game_icon.png here
    icon_img = pygame.image.load(icon_path)
    pygame.display.set_icon(icon_img)
except pygame.error as e:
    print(f"Warning: Could not load icon 'game_icon.ico'. {e}")

clock = pygame.time.Clock()
fps = 10

# ----------------- User Data Management -----------------
USER_DATA_FILE = os.path.join(base_path, "user_data.json")
current_user = None
user_data = {}

def load_user_data():
    global user_data
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r') as f:
                user_data = json.load(f)
        except json.JSONDecodeError:
            user_data = {}
    else:
        user_data = {}

def save_user_data():
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(user_data, f, indent=4)

def update_highscore(username, score):
    if username:
        if score > user_data.get(username, {}).get('highscore', 0):
            user_data[username]['highscore'] = score
            save_user_data()

# ----------------- Load Helpers -----------------
def load_and_scale(path, size):
    try:
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, size)
    except pygame.error as e:
        print(f"Error loading image at {path}: {e}")
        placeholder = pygame.Surface(size, pygame.SRCALPHA)
        placeholder.fill((255, 0, 255))
        return placeholder

def load_sound(path):
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    print(f"Warning: Sound file not found at {path}")
    return None

# ----------------- Load Assets -----------------
apple_img = load_and_scale(os.path.join(graphics_path, "apple.png"), (30, 30))
head_up_img = load_and_scale(os.path.join(graphics_path, "head_up.png"), (30, 30))
head_down_img = load_and_scale(os.path.join(graphics_path, "head_down.png"), (30, 30))
head_right_img = load_and_scale(os.path.join(graphics_path, "head_right.png"), (30, 30))
head_left_img = load_and_scale(os.path.join(graphics_path, "head_left.png"), (30, 30))
tail_up_img = load_and_scale(os.path.join(graphics_path, "tail_up.png"), (30, 30))
tail_down_img = load_and_scale(os.path.join(graphics_path, "tail_down.png"), (30, 30))
tail_right_img = load_and_scale(os.path.join(graphics_path, "tail_right.png"), (30, 30))
tail_left_img = load_and_scale(os.path.join(graphics_path, "tail_left.png"), (30, 30))
body_horizontal_img = load_and_scale(os.path.join(graphics_path, "body_horizontal.png"), (30, 30))
body_vertical_img = load_and_scale(os.path.join(graphics_path, "body_vertical.png"), (30, 30))
body_topright_img = load_and_scale(os.path.join(graphics_path, "body_topright.png"), (30, 30))
body_topleft_img = load_and_scale(os.path.join(graphics_path, "body_topleft.png"), (30, 30))
body_bottomright_img = load_and_scale(os.path.join(graphics_path, "body_bottomright.png"), (30, 30))
body_bottomleft_img = load_and_scale(os.path.join(graphics_path, "body_bottomleft.png"), (30, 30))
intro_img = load_and_scale(os.path.join(graphics_path, "Intro.png"), (screen_width, screen_height))
outro_img = load_and_scale(os.path.join(graphics_path, "Outro.png"), (screen_width, screen_height))
bg1_img = load_and_scale(os.path.join(graphics_path, "bg.png"), (screen_width, screen_height))
bg2_img = load_and_scale(os.path.join(graphics_path, "bg2.png"), (screen_width, screen_height))
bg_music = os.path.join(audio_path, "Baground.mp3")
eat_sound = load_sound(os.path.join(audio_path, "Beep.mp3"))
go_sound = load_sound(os.path.join(audio_path, "GameOver.mp3"))

# ----------------- Colors & Settings -----------------
COLOR_MAP = {"Blue": (0, 128, 255), "Green": (0, 200, 0), "White": (255, 255, 255), "Black": (0, 0, 0), "Yellow": (255, 255, 0)}
current_snake_color = "Blue"
current_bg = "bg1"

# ----------------- Sprite Tinting -----------------
def tint_image(image, color):
    tinted = image.copy()
    tint_surf = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    tint_surf.fill(color + (128,))
    tinted.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted

def apply_snake_color(color_name):
    global head_up_img, head_down_img, head_left_img, head_right_img
    global tail_up_img, tail_down_img, tail_left_img, tail_right_img
    global body_horizontal_img, body_vertical_img
    global body_topleft_img, body_topright_img, body_bottomleft_img, body_bottomright_img

    color = COLOR_MAP.get(color_name, COLOR_MAP["Blue"])
    head_up_img = tint_image(load_and_scale(os.path.join(graphics_path, "head_up.png"), (30,30)), color)
    head_down_img = tint_image(load_and_scale(os.path.join(graphics_path, "head_down.png"), (30,30)), color)
    head_left_img = tint_image(load_and_scale(os.path.join(graphics_path, "head_left.png"), (30,30)), color)
    head_right_img = tint_image(load_and_scale(os.path.join(graphics_path, "head_right.png"), (30,30)), color)
    tail_up_img = tint_image(load_and_scale(os.path.join(graphics_path, "tail_up.png"), (30,30)), color)
    tail_down_img = tint_image(load_and_scale(os.path.join(graphics_path, "tail_down.png"), (30,30)), color)
    tail_left_img = tint_image(load_and_scale(os.path.join(graphics_path, "tail_left.png"), (30,30)), color)
    tail_right_img = tint_image(load_and_scale(os.path.join(graphics_path, "tail_right.png"), (30,30)), color)
    body_horizontal_img = tint_image(load_and_scale(os.path.join(graphics_path, "body_horizontal.png"), (30,30)), color)
    body_vertical_img = tint_image(load_and_scale(os.path.join(graphics_path, "body_vertical.png"), (30,30)), color)
    body_topleft_img = tint_image(load_and_scale(os.path.join(graphics_path, "body_topleft.png"), (30,30)), color)
    body_topright_img = tint_image(load_and_scale(os.path.join(graphics_path, "body_topright.png"), (30,30)), color)
    body_bottomleft_img = tint_image(load_and_scale(os.path.join(graphics_path, "body_bottomleft.png"), (30,30)), color)
    body_bottomright_img = tint_image(load_and_scale(os.path.join(graphics_path, "body_bottomright.png"), (30,30)), color)

apply_snake_color(current_snake_color)

# ----------------- Snake Drawing -----------------
def draw_snake(snake_list, direction):
    if not snake_list:
        return
    head = snake_list[-1]
    head_map = {"up": head_up_img, "down": head_down_img, "left": head_left_img, "right": head_right_img}
    screen.blit(head_map.get(direction, head_right_img), head)
    if len(snake_list) > 1:
        tail = snake_list[0]
        neighbor = snake_list[1]
        if neighbor[0] > tail[0]: screen.blit(tail_left_img, tail)
        elif neighbor[0] < tail[0]: screen.blit(tail_right_img, tail)
        elif neighbor[1] > tail[1]: screen.blit(tail_up_img, tail)
        elif neighbor[1] < tail[1]: screen.blit(tail_down_img, tail)
    for i in range(1, len(snake_list) - 1):
        prev_block, current_block, next_block = snake_list[i-1], snake_list[i], snake_list[i+1]
        if prev_block[0] == next_block[0]:
            screen.blit(body_vertical_img, current_block)
        elif prev_block[1] == next_block[1]:
            screen.blit(body_horizontal_img, current_block)
        else:
            if (prev_block[0] < current_block[0] and next_block[1] < current_block[1]) or \
               (prev_block[1] < current_block[1] and next_block[0] < current_block[0]):
                screen.blit(body_topleft_img, current_block)
            elif (prev_block[0] > current_block[0] and next_block[1] < current_block[1]) or \
                 (prev_block[1] < current_block[1] and next_block[0] > current_block[0]):
                screen.blit(body_topright_img, current_block)
            elif (prev_block[0] < current_block[0] and next_block[1] > current_block[1]) or \
                 (prev_block[1] > current_block[1] and next_block[0] < current_block[0]):
                screen.blit(body_bottomleft_img, current_block)
            elif (prev_block[0] > current_block[0] and next_block[1] > current_block[1]) or \
                 (prev_block[1] > current_block[1] and next_block[0] > current_block[0]):
                screen.blit(body_bottomright_img, current_block)

# ----------------- Menus, Game Loop, and Main -----------------
font = pygame.font.SysFont(None, 48)
input_font = pygame.font.SysFont(None, 36)

def draw_text(text, pos, selected=False, color=COLOR_MAP["White"]):
    final_color = COLOR_MAP["Yellow"] if selected else color
    render = font.render(text, True, final_color)
    rect = render.get_rect(center=pos)
    screen.blit(render, rect)
    return rect

def play_music():
    if os.path.exists(bg_music):
        pygame.mixer.music.load(bg_music)
        pygame.mixer.music.play(-1)

def draw_input_box(prompt, text, rect, active):
    prompt_surf = font.render(prompt, True, COLOR_MAP["White"])
    screen.blit(prompt_surf, (rect.x, rect.y - 40))
    color = COLOR_MAP["Yellow"] if active else COLOR_MAP["White"]
    pygame.draw.rect(screen, color, rect, 2)
    text_surf = input_font.render(text, True, COLOR_MAP["White"])
    screen.blit(text_surf, (rect.x + 5, rect.y + 5))

def login_screen():
    global current_user
    username, password, message = "", "", ""
    user_box = pygame.Rect(screen_width//2 - 150, 200, 300, 40)
    pass_box = pygame.Rect(screen_width//2 - 150, 300, 300, 40)
    active_box = None
    buttons = {
        "Login": pygame.Rect(screen_width//2 - 155, 400, 150, 50),
        "Register": pygame.Rect(screen_width//2 + 5, 400, 150, 50),
        "Guest": pygame.Rect(screen_width//2 - 75, 460, 150, 50)
    }
    while True:
        screen.blit(intro_img, (0, 0))
        draw_input_box("Username:", username, user_box, active_box == 'user')
        draw_input_box("Password:", '*' * len(password), pass_box, active_box == 'pass')
        pygame.draw.rect(screen, COLOR_MAP["Green"], buttons["Login"])
        draw_text("Login", buttons["Login"].center)
        pygame.draw.rect(screen, COLOR_MAP["Blue"], buttons["Register"])
        draw_text("Register", buttons["Register"].center)
        pygame.draw.rect(screen, (100, 100, 100), buttons["Guest"])
        draw_text("Guest", buttons["Guest"].center)
        if message:
            draw_text(message, (screen_width//2, 550), color=COLOR_MAP["Yellow"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                active_box = None
                if user_box.collidepoint(event.pos): active_box = 'user'
                elif pass_box.collidepoint(event.pos): active_box = 'pass'
                if buttons["Login"].collidepoint(event.pos):
                    if username in user_data and user_data[username]['password'] == password:
                        current_user = username; return
                    else: message = "Invalid username or password"
                elif buttons["Register"].collidepoint(event.pos):
                    if username and password:
                        if username in user_data: message = "Username already exists"
                        else:
                            user_data[username] = {"password": password, "highscore": 0}
                            save_user_data(); message = "Account created! Please log in."
                            username, password = "", ""
                    else: message = "Enter username and password"
                elif buttons["Guest"].collidepoint(event.pos):
                    current_user = None; return
            if event.type == pygame.KEYDOWN and active_box:
                if event.key == pygame.K_BACKSPACE:
                    if active_box == 'user': username = username[:-1]
                    else: password = password[:-1]
                else:
                    if active_box == 'user': username += event.unicode
                    else: password += event.unicode
        pygame.display.update()
        clock.tick(30)

def intro_menu():
    global current_user
    play_music()
    options = ["Play", "Options", "Highscores", "Change Account", "Quit"] # <-- MODIFIED
    selected = 0
    while True:
        screen.blit(intro_img, (0, 0))
        if current_user:
            welcome_msg = f"Welcome, {current_user}!"
            highscore = user_data.get(current_user, {}).get('highscore', 0)
            score_msg = f"High Score: {highscore}"
            draw_text(welcome_msg, (screen_width // 2, 100))
            draw_text(score_msg, (screen_width // 2, 150))
        else:
            draw_text("Playing as Guest", (screen_width // 2, 100))
        rects = [draw_text(opt, (screen_width//2, 240 + i*60), i == selected) for i, opt in enumerate(options)]
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN: selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected].lower().replace(" ", "_")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, r in enumerate(rects):
                    if r.collidepoint(event.pos):
                        return options[i].lower().replace(" ", "_")

def options_menu():
    global current_snake_color, current_bg
    selected = 0
    colors = list(COLOR_MAP.keys())
    while True:
        screen.blit(bg1_img if current_bg == "bg1" else bg2_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: selected = (selected - 1) % 3
                elif event.key == pygame.K_DOWN: selected = (selected + 1) % 3
                elif event.key == pygame.K_RETURN:
                    if selected == 2: return
                elif event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    if selected == 0:
                        idx = colors.index(current_snake_color)
                        idx = (idx + (1 if event.key == pygame.K_RIGHT else -1)) % len(colors)
                        current_snake_color = colors[idx]
                        apply_snake_color(current_snake_color)
                    elif selected == 1:
                        current_bg = "bg2" if current_bg == "bg1" else "bg1"
        options = [f"Snake Color: {current_snake_color}", f"Background: {current_bg}", "Back"]
        draw_text("Options", (screen_width // 2, 100))
        [draw_text(opt, (screen_width // 2, 250 + i * 60), i == selected) for i, opt in enumerate(options)]
        pygame.display.update()
        clock.tick(30)

# <-- NEW FUNCTION
def highscore_screen():
    """Displays a ranked list of the top 10 highscores."""
    scores = [(username, data.get('highscore', 0)) for username, data in user_data.items()]
    sorted_scores = sorted(scores, key=lambda item: item[1], reverse=True)
    waiting = True
    while waiting:
        screen.blit(intro_img, (0, 0))
        draw_text("Leaderboard", (screen_width // 2, 80))
        for i, (username, score) in enumerate(sorted_scores[:10]):
            rank_text = f"{i + 1}. {username} - {score}"
            draw_text(rank_text, (screen_width // 2, 150 + i * 40), color=COLOR_MAP["White"])
        draw_text("Press any key to return", (screen_width // 2, 550), color=COLOR_MAP["Yellow"])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN: waiting = False

def game_over_screen(score):
    pygame.mixer.music.stop()
    if go_sound: go_sound.play()
    screen.blit(outro_img, (0, 0))
    draw_text(f"Your Score: {score}", (screen_width//2, 300))
    if current_user:
        highscore = user_data.get(current_user, {}).get('highscore', 0)
        draw_text(f"High Score: {highscore}", (screen_width//2, 360))
    draw_text("Press any key to continue", (screen_width//2, 500))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                waiting = False

def gameloop():
    snake_x, snake_y = screen_width // 2, screen_height // 2
    x_velocity, y_velocity = 0, 0
    direction = "right"
    snake_list, snake_length = [[snake_x, snake_y]], 1
    apple_x = random.randrange(0, screen_width - 30, 30)
    apple_y = random.randrange(0, screen_height - 30, 30)
    score = 0
    game_over = False
    while not game_over:
        bg_img = bg1_img if current_bg == "bg1" else bg2_img
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a] and x_velocity == 0:
                    x_velocity, y_velocity, direction = -30, 0, "left"
                elif event.key in [pygame.K_RIGHT, pygame.K_d] and x_velocity == 0:
                    x_velocity, y_velocity, direction = 30, 0, "right"
                elif event.key in [pygame.K_UP, pygame.K_w] and y_velocity == 0:
                    x_velocity, y_velocity, direction = 0, -30, "up"
                elif event.key in [pygame.K_DOWN, pygame.K_s] and y_velocity == 0:
                    x_velocity, y_velocity, direction = 0, 30, "down"
        snake_x += x_velocity
        snake_y += y_velocity
        head = [snake_x, snake_y]
        if head in snake_list: game_over = True
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        if pygame.Rect(snake_x, snake_y, 30, 30).colliderect(pygame.Rect(apple_x, apple_y, 30, 30)):
            if eat_sound: eat_sound.play()
            snake_length += 1
            score += 1
            apple_x, apple_y = random.randrange(0, screen_width // 30) * 30, random.randrange(0, screen_height // 30) * 30
        if not (0 <= snake_x < screen_width and 0 <= snake_y < screen_height):
            game_over = True
        screen.blit(bg_img, (0, 0))
        screen.blit(apple_img, (apple_x, apple_y))
        draw_snake(snake_list, direction)
        draw_text(f"Score: {score}", (100, 30))
        pygame.display.update()
        clock.tick(fps)
    update_highscore(current_user, score)
    game_over_screen(score)

if __name__ == "__main__":
    load_user_data()
    while True:
        login_screen()
        while True:
            choice = intro_menu()
            if choice == "play": gameloop()
            elif choice == "options": options_menu()
            elif choice == "highscores": highscore_screen() # <-- MODIFIED
            elif choice == "change_account": current_user = None; break
            elif choice == "quit": pygame.quit(); sys.exit()