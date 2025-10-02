import random
import sys
import pygame
from pygame.locals import *

# Initialize all pygame modules
pygame.init()     
pygame.mixer.init()

# Game setup - FIXED SIZE
FPS = 32
screen_width = 289
screen_height = 511
# Set a FIXED-SIZE screen
screen = pygame.display.set_mode((screen_width, screen_height)) 
GROUNDY = screen_height * 0.8
GAME_SPRITE = {}
GAME_SOUND = {}

# Paths to game assets
PLAYER = r"gallery/sprites/bird.png"
BACKGROUND = r"gallery/sprites/background.png"
PIPE = r"gallery/sprites/pipe.png"

FPSCLOCK = pygame.time.Clock()


def Welcome():
    """Shows the welcome screen until a key is pressed."""
    PLAYERX = int(screen_width / 5)
    PLAYERY = int((screen_height - GAME_SPRITE["PLAYER"].get_height()) / 2)
    MessageX = int((screen_width - GAME_SPRITE["message"].get_width()) / 2)
    MessageY = int(screen_height * 0.13)
    BASEX = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return 
        

        screen.blit(GAME_SPRITE["BACKGROUND"], (0, 0))
        screen.blit(GAME_SPRITE["PLAYER"], (PLAYERX, PLAYERY))
        screen.blit(GAME_SPRITE["message"], (MessageX, MessageY))
        screen.blit(GAME_SPRITE["BASE"], (BASEX, GROUNDY))
        

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getRandomPipe():
    """Generates the positions for a new pair of pipes."""
    pipe_height = GAME_SPRITE["PIPE"][0].get_height()
    gap_size = 100


    lower_pipe_y = random.randrange(int(screen_height / 3), int(GROUNDY - 50))
    upper_pipe_y = lower_pipe_y - gap_size - pipe_height

    pipeX = screen_width + 10
    pipe = [
        {"x": pipeX, "y": upper_pipe_y},  # Upper Pipe
        {"x": pipeX, "y": lower_pipe_y}  # Lower Pipe
    ]
    return pipe

def isCollide(PLAYERX, PLAYERY, upper_pipes, lower_pipes):
    player_height = GAME_SPRITE["PLAYER"].get_height()
    player_width = GAME_SPRITE["PLAYER"].get_width()
    pipe_width = GAME_SPRITE["PIPE"][0].get_width()

    # Collision with ground or ceiling
    if PLAYERY > GROUNDY - player_height or PLAYERY < 0:
        GAME_SOUND["GameOver"].play()
        return True
    
    for pipe in upper_pipes:
        pipe_height = GAME_SPRITE["PIPE"][0].get_height()
        # Collision check with upper pipe
        if (PLAYERY < pipe_height + pipe["y"] and 
            abs(PLAYERX - pipe["x"]) < pipe_width):
            GAME_SOUND["GameOver"].play()
            return True
            
    for pipe in lower_pipes:
        # Collision check with lower pipe
        if (PLAYERY + player_height > pipe["y"] and 
            abs(PLAYERX - pipe["x"]) < pipe_width):
            GAME_SOUND["GameOver"].play()
            return True


    return False

def maingame():
    SCORE = 0
    PLAYERX = int(screen_width / 5)
    PLAYERY = int(screen_height / 2)
    basex = -((-basex + 4) % GAME_SPRITE["BASE"].get_width())
    screen.blit(GAME_SPRITE["BASE"], (basex, GROUNDY))
    screen.blit(GAME_SPRITE["BASE"], (basex + GAME_SPRITE["BASE"].get_width(), GROUNDY))


    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # Lists of upper and lower pipes
    Upperpipe = [
        {"x": screen_width + 200, "y": newPipe1[0]["y"]},
        {"x": screen_width + 200 + (screen_width / 2), "y": newPipe2[0]["y"]}
    ]
    Lowerpipe = [
        {"x": screen_width + 200, "y": newPipe1[1]["y"]},
        {"x": screen_width + 200 + (screen_width / 2), "y": newPipe2[1]["y"]}
    ]

    pipevelX = -4
    playervelY = -9
    playerMaxY = 10
    playerAccY = 1
    playerFlapAccv = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if PLAYERY > 0:
                    playervelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUND["wing"].play()

        crashTest = isCollide(PLAYERX, PLAYERY, Upperpipe, Lowerpipe)
        if crashTest:
            return  # End the main game and return to the welcome screen

        # Check for score
        PlayerMidPos = PLAYERX + GAME_SPRITE["PLAYER"].get_width() / 2
        for pipe in Upperpipe:
            pipeMidPos = pipe["x"] + GAME_SPRITE["PIPE"][0].get_width() / 2
            if pipeMidPos <= PlayerMidPos < pipeMidPos + abs(pipevelX):
                SCORE += 1
                GAME_SOUND["Score"].play()

        if playervelY < playerMaxY and not playerFlapped:
            playervelY += playerAccY
        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITE["PLAYER"].get_height()
        PLAYERY += min(playervelY, GROUNDY - PLAYERY - playerHeight)

        # Move pipes to the left
        for uPipe, lPipe in zip(Upperpipe, Lowerpipe):
            uPipe["x"] += pipevelX
            lPipe["x"] += pipevelX

        # Add a new pipe when the first one is about to leave the screen
        if 0 < Upperpipe[0]["x"] < 5:
            newPipe = getRandomPipe()
            Upperpipe.append(newPipe[0])
            Lowerpipe.append(newPipe[1])

        # Remove the pipe that has gone off-screen
        if Upperpipe[0]["x"] < -GAME_SPRITE["PIPE"][0].get_width():
            Upperpipe.pop(0)
            Lowerpipe.pop(0)

        # Blit all sprites
        screen.blit(GAME_SPRITE["BACKGROUND"], (0, 0))
        for uPipe, lPipe in zip(Upperpipe, Lowerpipe):
            screen.blit(GAME_SPRITE["PIPE"][0], (uPipe["x"], uPipe["y"]))
            screen.blit(GAME_SPRITE["PIPE"][1], (lPipe["x"], lPipe["y"]))
        screen.blit(GAME_SPRITE["BASE"], (basex, GROUNDY))
        screen.blit(GAME_SPRITE["PLAYER"], (PLAYERX, PLAYERY))
        
        myDigits = [int(x) for x in str(SCORE)]
        width = sum(GAME_SPRITE["numbers"][digit].get_width() for digit in myDigits)
        Xoffset = (screen_width - width) / 2

        for digit in myDigits:
            screen.blit(GAME_SPRITE["numbers"][digit], (Xoffset, screen_height * 0.12))
            Xoffset += GAME_SPRITE["numbers"][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    pygame.display.set_caption("Flappy Bird by Abhigyan")
    
    GAME_SPRITE["numbers"] = tuple(
        pygame.image.load(f"gallery/sprites/{i}.png").convert_alpha() 
        for i in range(10)
    )

    GAME_SPRITE["message"] = pygame.image.load("gallery/sprites/message.png").convert_alpha()

    GAME_SPRITE["BASE"] = pygame.image.load("gallery/sprites/base.png").convert_alpha()
    pipe_image = pygame.image.load(PIPE).convert_alpha()
    GAME_SPRITE["PIPE"] = (pygame.transform.rotate(pipe_image, 180), pipe_image)
    GAME_SPRITE["PLAYER"] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITE["BACKGROUND"] = pygame.image.load(BACKGROUND).convert() 

    GAME_SOUND["wing"] = pygame.mixer.Sound("gallery/audio/wing.wav")
    GAME_SOUND["Score"] = pygame.mixer.Sound("gallery/audio/score.wav")
    GAME_SOUND["GameOver"] = pygame.mixer.Sound("gallery/audio/GameOver.wav")
    
    
    # Main game loop
    while True:
        Welcome()
        maingame()
