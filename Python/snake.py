import pygame
import random

# Window dimensions
WIDTH = 800
HEIGHT = 600

# Snake properties
SNAKE_LENGTH = 10
SNAKE_SIZE = 20
SNAKE_COLOR = (0, 255, 0)   # Green

# Food properties
FOOD_SIZE = 10
FOOD_COLOR = (255, 0, 0)   # Red

# Game variables
snake_position = [(WIDTH // 2, HEIGHT // 2) for _ in range(SNAKE_LENGTH)]
direction = 'right'
score = 0
game_over = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                direction = 'down'

    # Move the snake
    if direction == 'left':
        new_head = (snake_position[0][0] - SNAKE_SIZE, snake_position[0][1])
    elif direction == 'right':
        new_head = (snake_position[0][0] + SNAKE_SIZE, snake_position[0][1])
    elif direction == 'up':
        new_head = (snake_position[0][0], snake_position[0][1] - SNAKE_SIZE)
    elif direction == 'down':
        new_head = (snake_position[0][0], snake_position[0][1] + SNAKE_SIZE)

    snake_position.insert(0, new_head)

    # Check for collisions
    if snake_position[0] in [pos for pos in snake_position[1:]]:
        game_over = True

    # Generate food
    food_x = random.randint(0, (WIDTH // SNAKE_SIZE) - 1) * SNAKE_SIZE
    food_y = random.randint(0, (HEIGHT // SNAKE_SIZE) - 1) * SNAKE_SIZE

    # Draw everything
    screen.fill((255, 255, 255))  # Clear the screen

    for pos in snake_position:
        pygame.draw.rect(screen, SNAKE_COLOR, (pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.draw.rect(screen, FOOD_COLOR, (food_x, food_y, FOOD_SIZE, FOOD_SIZE))

    # Update the screen
    pygame.display.flip()
    clock.tick(60)

    if game_over:
        print("Game Over! Score:", score)
        pygame.quit()
        quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()