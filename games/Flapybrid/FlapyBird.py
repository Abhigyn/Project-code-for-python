import random
import sys
import pygame
from pygame.locals import *

# --- Constants ---
FPS = 32
SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511
GROUND_Y = SCREEN_HEIGHT * 0.8
PIPE_GAP_SIZE = 100  # Gap between upper and lower pipe

# --- Game Assets ---
ASSETS = {
    "player": "gallery/sprites/bluebird-midflap.png",
    "background": "gallery/sprites/background-day.png",
    "pipe": "gallery/sprites/pipe-green.png",
    "base": "gallery/sprites/base.png",
    "message": "gallery/sprites/message.png",
    "numbers": tuple(f"gallery/sprites/{i}.png" for i in range(10)),
    "sounds": {
        "wing": "gallery/audio/wing.wav",
        "score": "gallery/audio/score.wav",
        "gameover": "gallery/audio/GameOver.wav"
    }
}

# --- Global Dictionaries ---
GAME_SPRITES = {}
GAME_SOUNDS = {}

def load_assets():
    """Loads all game images and sounds into the global dictionaries."""
    # Load images
    GAME_SPRITES["numbers"] = tuple(
        pygame.image.load(path).convert_alpha() for path in ASSETS["numbers"]
    )
    GAME_SPRITES["message"] = pygame.image.load(ASSETS["message"]).convert_alpha()
    GAME_SPRITES["base"] = pygame.image.load(ASSETS["base"]).convert_alpha()
    GAME_SPRITES["player"] = pygame.image.load(ASSETS["player"]).convert_alpha()
    GAME_SPRITES["background"] = pygame.image.load(ASSETS["background"]).convert()
    
    pipe_image = pygame.image.load(ASSETS["pipe"]).convert_alpha()
    GAME_SPRITES["pipe"] = (
        pygame.transform.rotate(pipe_image, 180),  # Upper pipe
        pipe_image                                  # Lower pipe
    )
    
    # Load sounds
    for name, path in ASSETS["sounds"].items():
            GAME_SOUNDS[name] = pygame.mixer.Sound(path)



def welcome_screen():
    """Shows the welcome screen until the user starts the game."""
    player_x = int(SCREEN_WIDTH / 5)
    player_y = int((SCREEN_HEIGHT - GAME_SPRITES["player"].get_height()) / 2)
    message_x = int((SCREEN_WIDTH - GAME_SPRITES["message"].get_width()) / 2)
    message_y = int(SCREEN_HEIGHT * 0.13)
    base_x = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

        screen.blit(GAME_SPRITES["background"], (0, 0))
        # screen.blit(GAME_SPRITES["player"], (player_x, player_y))
        screen.blit(GAME_SPRITES["message"], (message_x, message_y))
        screen.blit(GAME_SPRITES["base"], (base_x, GROUND_Y))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def main_game():
    """The main gameplay loop."""
    score = 0
    player_x = int(SCREEN_WIDTH / 5)
    player_y = int(SCREEN_HEIGHT / 2)
    base_x = 0
    base_shift_speed = 4

    # Player physics parameters
    player_vel_y = -9
    player_max_vel_y = 10
    player_acc_y = 1
    player_flap_accv = -8
    player_flapped = False

    # Create two initial pipes
    pipe1 = get_random_pipe()
    pipe2 = get_random_pipe()

    upper_pipes = [
        {"x": SCREEN_WIDTH + 200, "y": pipe1[0]["y"]},
        {"x": SCREEN_WIDTH + 200 + (SCREEN_WIDTH / 2), "y": pipe2[0]["y"]},
    ]
    lower_pipes = [
        {"x": SCREEN_WIDTH + 200, "y": pipe1[1]["y"]},
        {"x": SCREEN_WIDTH + 200 + (SCREEN_WIDTH / 2), "y": pipe2[1]["y"]},
    ]

    pipe_vel_x = -4

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP or event.key == K_w):
                if player_y > 0:
                    player_vel_y = player_flap_accv
                    player_flapped = True
                    GAME_SOUNDS["wing"].play()

        if is_collision(player_x, player_y, upper_pipes, lower_pipes):
            GAME_SOUNDS["gameover"].play()
            return  # Game Over

        # Score logic
        player_mid_pos = player_x + GAME_SPRITES["player"].get_width() / 2
        for pipe in upper_pipes:
            pipe_mid_pos = pipe["x"] + GAME_SPRITES["pipe"][0].get_width() / 2
            if pipe_mid_pos <= player_mid_pos < pipe_mid_pos + abs(pipe_vel_x):
                score += 1
                GAME_SOUNDS["score"].play()

        # Player movement
        if player_vel_y < player_max_vel_y and not player_flapped:
            player_vel_y += player_acc_y
        if player_flapped:
            player_flapped = False
        
        player_height = GAME_SPRITES["player"].get_height()
        player_y += min(player_vel_y, GROUND_Y - player_y - player_height)

        # Pipe movement
        for u_pipe, l_pipe in zip(upper_pipes, lower_pipes):
            u_pipe["x"] += pipe_vel_x
            l_pipe["x"] += pipe_vel_x

        # Add a new pipe
        if 0 < upper_pipes[0]["x"] < 5:
            new_pipe = get_random_pipe()
            upper_pipes.append(new_pipe[0])
            lower_pipes.append(new_pipe[1])

        # Remove old pipes
        if upper_pipes[0]["x"] < -GAME_SPRITES["pipe"][0].get_width():
            upper_pipes.pop(0)
            lower_pipes.pop(0)

        # Base movement (creates scrolling effect)
        base_x = (base_x - base_shift_speed) % GAME_SPRITES['base'].get_width()

        # --- Drawing ---
        screen.blit(GAME_SPRITES["background"], (0, 0))
        for u_pipe, l_pipe in zip(upper_pipes, lower_pipes):
            screen.blit(GAME_SPRITES["pipe"][0], (u_pipe["x"], u_pipe["y"]))
            screen.blit(GAME_SPRITES["pipe"][1], (l_pipe["x"], l_pipe["y"]))
        
        # Blit two base images for a seamless scroll
        screen.blit(GAME_SPRITES["base"], (-base_x, GROUND_Y))
        screen.blit(GAME_SPRITES["base"], (GAME_SPRITES['base'].get_width() - base_x, GROUND_Y))

        screen.blit(GAME_SPRITES["player"], (player_x, player_y))
        draw_score(score)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def get_random_pipe():
    """Generates positions for a new pair of pipes."""
    pipe_height = GAME_SPRITES["pipe"][0].get_height()
    
    # Randomly position the lower pipe, ensuring it's not too high or too low
    lower_pipe_y = random.randrange(int(SCREEN_HEIGHT / 3), int(GROUND_Y - 1.2 * PIPE_GAP_SIZE))
    upper_pipe_y = lower_pipe_y - PIPE_GAP_SIZE - pipe_height

    pipe_x = SCREEN_WIDTH + 10
    return [
        {"x": pipe_x, "y": upper_pipe_y},  # Upper Pipe
        {"x": pipe_x, "y": lower_pipe_y},  # Lower Pipe
    ]

def is_collision(player_x, player_y, upper_pipes, lower_pipes):
    """Checks for collision using Rect objects for better accuracy."""
    player_rect = GAME_SPRITES["player"].get_rect(topleft=(player_x, player_y))

    # Check for collision with ground or ceiling
    if player_rect.top <= 0 or player_rect.bottom >= GROUND_Y:
        return True

    # Check for collision with pipes
    for u_pipe, l_pipe in zip(upper_pipes, lower_pipes):
        u_pipe_rect = GAME_SPRITES["pipe"][0].get_rect(topleft=(u_pipe['x'], u_pipe['y']))
        l_pipe_rect = GAME_SPRITES["pipe"][1].get_rect(topleft=(l_pipe['x'], l_pipe['y']))
        if player_rect.colliderect(u_pipe_rect) or player_rect.colliderect(l_pipe_rect):
            return True

    return False

def draw_score(score):
    """Renders the score on the screen."""
    score_digits = [int(x) for x in str(score)]
    total_width = sum(GAME_SPRITES["numbers"][digit].get_width() for digit in score_digits)
    x_offset = (SCREEN_WIDTH - total_width) / 2

    for digit in score_digits:
        screen.blit(GAME_SPRITES["numbers"][digit], (x_offset, SCREEN_HEIGHT * 0.12))
        x_offset += GAME_SPRITES["numbers"][digit].get_width()

# --- Main Execution ---
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    FPSCLOCK = pygame.time.Clock()
    
    pygame.display.set_caption("Flappy Bird by Gemini")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    load_assets()

    while True:
        welcome_screen()
        main_game()