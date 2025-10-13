import pygame
from sys import exit
from random import randint, choice

pygame.init()

# --- Classes ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load player animations
        player_walk_1 = pygame.image.load("a/graphics/Player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("a/graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_jump = pygame.image.load("a/graphics/Player/jump.png").convert_alpha()
        self.player_index = 0
        
        # Initial setup
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300)) # Changed from (200, 300) to (80, 300) for better start
        self.gravity = 0
        
        # Sound setup
        self.jump_music = pygame.mixer.Sound("a/audio/jump.mp3")
        self.jump_music.set_volume(0.5)

    def player_input(self):
        Keys = pygame.key.get_pressed()
        # Check for both space and up arrow
        if (Keys[pygame.K_SPACE] or Keys[pygame.K_UP]) and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_music.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0 # Reset gravity when on the ground

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump # Jump state
        else:
            # Walk state
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): 
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        # Load obstacle animations
        if type == "fly":
            fly_frame1 = pygame.image.load("a\graphics\Fly\Fly1.png").convert_alpha()
            fly_frame2 = pygame.image.load("a\graphics\Fly\Fly2.png").convert_alpha()
            self.frames = [fly_frame1, fly_frame2]
            y_pos = 210
        else: # Assumes "snail" if not "fly"
            snail_frame1 = pygame.image.load("a/graphics/snail/snail1.png").convert_alpha()
            snail_frame2 = pygame.image.load("a/graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): 
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.Destroy()

    def Destroy(self):
        # Remove sprite when it moves off-screen
        if self.rect.x <= -100:
            self.kill()

# --- Game Setup ---
Screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pixwlrunner")
CLOCK = pygame.time.Clock()

# Game State Variables
Start_time = 0
Score = 0
Game_active = False # Start in the intro screen

# Background Music
bg_music = pygame.mixer.Sound("a/audio/music.wav")
bg_music.play(loops=-1)

# Font Setup
fount1_Fonts = pygame.font.Font(r"a\font\Pixeltype.ttf", 50)

# Surfaces
Sky_surface = pygame.image.load("a/graphics/sky.png").convert()
Ground_surface = pygame.image.load("a/graphics/ground.png").convert()

# Intro Screen Player Image
player_stand = pygame.image.load("a/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

# Intro Screen Text
Game_name = fount1_Fonts.render("Pixel Runer", False, (111, 196, 169))
Game_name_rect = Game_name.get_rect(center=(400, 80))
Game_ins = fount1_Fonts.render("Press space or UP arrow key to start", False, (111, 196, 169))
Game_ins_rect = Game_ins.get_rect(center=(400, 320))

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
Obstacle_group = pygame.sprite.Group()

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) # Spawns a new obstacle every 1.5 seconds

# --- Functions ---
def score():
    """Calculates and displays the current score."""
    current_time = int(pygame.time.get_ticks() / 1000) - Start_time
    score_surf = fount1_Fonts.render(f"Score: {current_time}", False, (255, 0, 0))
    score_rect = score_surf.get_rect(center=(400, 50))
    Screen.blit(score_surf, score_rect)
    return current_time

def collisionn():
    """Checks for collision between the player and any obstacle."""
    # spritecollide returns a list of sprites that intersect with the player sprite
    if pygame.sprite.spritecollide(player.sprite, Obstacle_group, False):
        Obstacle_group.empty()
        return False  # Collision detected
    else:
        return True  # No collision

# --- Game Loop ---
while True:
    # 1. EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if Game_active:
            # Obstacle spawning timer
            if event.type == obstacle_timer:
                # 1/4 chance for a fly, 3/4 chance for a snail
                Obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
        else: # Not Game_active (Intro/Game Over screen)
            # Restart game on space, up key, or mouse click
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
                Game_active = True
                player.sprite.rect.midbottom = (80, 300) 
                Start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.MOUSEBUTTONDOWN:
                Game_active = True
                player.sprite.rect.midbottom = (80, 300) 
                Start_time = int(pygame.time.get_ticks() / 1000)
                
    
    
    
    if Game_active:
        Game_active = collisionn() 
        Score = score()
        player.update()
        Obstacle_group.update()
        
    # 2. DRAWING
    if Game_active:
        Screen.blit(Sky_surface, (0, 0))
        Screen.blit(Ground_surface, (0, 300))
        score()
        
        # Draw and update sprites
        player.draw(Screen)
        Obstacle_group.draw(Screen)
        
    else: # Game Over / Intro Screen
        Screen.fill((94, 129, 162))
        Screen.blit(player_stand, player_stand_rect)

        # Game Over/Score Text
        score_message = fount1_Fonts.render(f"Score: {Score}", False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center=(400, 350))

        Screen.blit(Game_name, Game_name_rect)
        Screen.blit(Game_ins, Game_ins_rect)
        
        # Only display the score after a game has been played (Score > 0 or Start_time > 0)
        if Score > 0 or Start_time > 0:
             Screen.blit(score_message, score_message_rect)
        if event.type == pygame.K_SPACE or event.type == pygame.K_UP:
            Game_active = collisionn

    # 4. DISPLAY UPDATE and FRAMERATE CAP
    pygame.display.update()
    CLOCK.tick(60)