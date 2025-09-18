import pygame
import random
import os

pygame.init()

# ----------------- Screen Setup -----------------
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with Sprites")

clock = pygame.time.Clock()
fps = 15

# ----------------- Colors -----------------
white = (255, 255, 255)
bg_color = (175, 215, 70) 

# ----------------- Asset Loader -----------------
def load_and_scale(path, size=(40, 40)):
    return pygame.transform.scale(pygame.image.load(path).convert_alpha(), size)

# Correct folder path
graphics_path = os.path.join(os.path.dirname(__file__), "snake_graphics")

# Apple
apple_img = load_and_scale(os.path.join(graphics_path, "apple.png"))

# Snake Head
head_up_img = load_and_scale(os.path.join(graphics_path, "head_up.png"))
head_down_img = load_and_scale(os.path.join(graphics_path, "head_down.png"))
head_left_img = load_and_scale(os.path.join(graphics_path, "head_left.png"))
head_right_img = load_and_scale(os.path.join(graphics_path, "head_right.png"))

# Snake Tail
tail_up_img = load_and_scale(os.path.join(graphics_path, "tail_up.png"))
tail_down_img = load_and_scale(os.path.join(graphics_path, "tail_down.png"))
tail_left_img = load_and_scale(os.path.join(graphics_path, "tail_left.png"))
tail_right_img = load_and_scale(os.path.join(graphics_path, "tail_right.png"))

# Snake Body
body_vertical_img = load_and_scale(os.path.join(graphics_path, "body_vertical.png"))
body_horizontal_img = load_and_scale(os.path.join(graphics_path, "body_horizontal.png"))
body_topleft_img = load_and_scale(os.path.join(graphics_path, "body_topleft.png"))
body_topright_img = load_and_scale(os.path.join(graphics_path, "body_topright.png"))
body_bottomleft_img = load_and_scale(os.path.join(graphics_path, "body_bottomleft.png"))
body_bottomright_img = load_and_scale(os.path.join(graphics_path, "body_bottomright.png"))

# ----------------- Snake Drawing -----------------
def draw_snake(snake_list, velocity_x, velocity_y):
    """Draws the snake on the screen, selecting the correct sprites."""
    if not snake_list:
        return
        
    # Draw head based on velocity
    if velocity_x > 0:
        screen.blit(head_right_img, snake_list[0])
    elif velocity_x < 0:
        screen.blit(head_left_img, snake_list[0])
    elif velocity_y > 0:
        screen.blit(head_down_img, snake_list[0])
    elif velocity_y < 0:
        screen.blit(head_up_img, snake_list[0])
    else:  # Draw a default head if not moving
        screen.blit(head_right_img, snake_list[0])

    # Draw body and tail
    if len(snake_list) > 1:
        for i in range(1, len(snake_list)):
            current_segment = snake_list[i]
            
            # Draw tail
            if i == len(snake_list) - 1:
                prev_segment = snake_list[i-1]
                if prev_segment[0] > current_segment[0]:
                    screen.blit(tail_left_img, current_segment)
                elif prev_segment[0] < current_segment[0]:
                    screen.blit(tail_right_img, current_segment)
                elif prev_segment[1] > current_segment[1]:
                    screen.blit(tail_up_img, current_segment)
                elif prev_segment[1] < current_segment[1]:
                    screen.blit(tail_down_img, current_segment)
            # Draw body segments
            else:
                prev_segment = snake_list[i-1]
                next_segment = snake_list[i+1]
                
                # Straight segments
                if prev_segment[0] == next_segment[0]:
                    screen.blit(body_vertical_img, current_segment)
                elif prev_segment[1] == next_segment[1]:
                    screen.blit(body_horizontal_img, current_segment)
                # Corner segments
                else:
                    if (prev_segment[0] < current_segment[0] and next_segment[1] < current_segment[1]) or \
                       (next_segment[0] < current_segment[0] and prev_segment[1] < current_segment[1]):
                        screen.blit(body_bottomright_img, current_segment)
                    elif (prev_segment[0] < current_segment[0] and next_segment[1] > current_segment[1]) or \
                         (next_segment[0] < current_segment[0] and prev_segment[1] > current_segment[1]):
                        screen.blit(body_topright_img, current_segment)
                    elif (prev_segment[0] > current_segment[0] and next_segment[1] < current_segment[1]) or \
                         (next_segment[0] > current_segment[0] and prev_segment[1] < current_segment[1]):
                        screen.blit(body_bottomleft_img, current_segment)
                    elif (prev_segment[0] > current_segment[0] and next_segment[1] > current_segment[1]) or \
                         (next_segment[0] > current_segment[0] and prev_segment[1] > current_segment[1]):
                        screen.blit(body_topleft_img, current_segment)

# ----------------- Game Loop -----------------
def gameloop():
    snake_x = 100
    snake_y = 100
    velocity_x = 0
    velocity_y = 0
    snake_list = [[snake_x, snake_y]]
    snake_length = 1

    apple_x = random.randrange(0, screen_width - 40, 40)
    apple_y = random.randrange(0, screen_height - 40, 40)

    game_over = False
    game_started = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if not game_started:
                    game_started = True

                # These checks are now at the correct indentation level
                if event.key == pygame.K_RIGHT and velocity_x == 0:
                    velocity_x = 40
                    velocity_y = 0
                elif event.key == pygame.K_LEFT and velocity_x == 0:
                    velocity_x = -40
                    velocity_y = 0
                elif event.key == pygame.K_UP and velocity_y == 0:
                    velocity_y = -40
                    velocity_x = 0
                elif event.key == pygame.K_DOWN and velocity_y == 0:
                    velocity_y = 40
                    velocity_x = 0
        
        # This movement logic must run every frame
        if game_started:
            snake_x += velocity_x
            snake_y += velocity_y
            head = [snake_x, snake_y]
            snake_list.insert(0, head)

            if len(snake_list) > snake_length:
                snake_list.pop()

            if snake_x == apple_x and snake_y == apple_y:
                snake_length += 1
                apple_x = random.randrange(0, screen_width - 40, 40)
                apple_y = random.randrange(0, screen_height - 40, 40)

            if snake_x < 0 or snake_x >= screen_width or snake_y < 0 or snake_y >= screen_height:
                game_over = True

            if head in snake_list[1:]:
                game_over = True

        screen.fill(bg_color)
        screen.blit(apple_img, (apple_x, apple_y))
        
        draw_snake(snake_list, velocity_x, velocity_y)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

# ----------------- Run -----------------
if __name__ == "__main__":
    gameloop()