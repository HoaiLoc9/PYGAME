import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Màu sắc
WHITE, GREEN, RED = (255, 255, 255), (0, 255, 0), (255, 0, 0)

# Kích thước rắn
snake_block = 10
snake_speed = 15

# Font chữ
font = pygame.font.Font(None, 36)

def gameLoop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake = [(x, y)]
    food = (random.randrange(0, WIDTH, snake_block), random.randrange(0, HEIGHT, snake_block))
    score = 0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            text = font.render("Game Over! Nhấn R để chơi lại", True, RED)
            screen.blit(text, (WIDTH // 6, HEIGHT // 3))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        x += dx
        y += dy
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        snake.insert(0, (x, y))
        if x == food[0] and y == food[1]:
            score += 1
            food = (random.randrange(0, WIDTH, snake_block), random.randrange(0, HEIGHT, snake_block))
        else:
            snake.pop()

        if (x, y) in snake[1:]:
            game_close = True

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, RED, (*food, snake_block, snake_block))
        for block in snake:
            pygame.draw.rect(screen, GREEN, (*block, snake_block, snake_block))

        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(snake_speed + score)

    pygame.quit()

gameLoop()
