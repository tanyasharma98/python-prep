import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 500

# Color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))  # Setting display window width and height
pygame.display.set_caption("Tanya-Snake")
pygame.display.update()

# Setting variables
exit_game = False  # True when exiting the game
game_over = False  # True when game over
snake_x = 43
snake_y = 50
velocity_x = 0
velocity_y = 0
init_velocity = 5
half_w = int(screen_width / 2)
half_h = int(screen_height / 2)
food_x = random.randint(15, half_w)
food_y = random.randint(15, half_h)
snake_size = 20
score = 0
fps = 70  # frame per second

clock = pygame.time.Clock()
# Creating loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # snake_x = snake_x + 10
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                # snake_x = snake_x - 10
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                # snake_y = snake_y - 10
                velocity_y = -init_velocity
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                # snake_y = snake_y + 10
                velocity_y = init_velocity
                velocity_x = 0
    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
        score += 1
        print(f"Score : {score*10}")
        food_x = random.randint(15, half_w)
        food_y = random.randint(15, half_h)

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
