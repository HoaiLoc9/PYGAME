import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Né chướng ngại vật")

player_x = WIDTH // 2 - 25
player_y = HEIGHT - 100
player_width = 50
player_height = 60
player_speed = 5

obstacle_x = random.randint(0, WIDTH - 50)
obstacle_y = -50
obstacle_speed = 5
obstacle_width = 50
obstacle_height = 50

running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -50
        obstacle_x = random.randint(0, WIDTH - obstacle_width)

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        print("Game Over!")
        running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pygame.display.update()

pygame.quit()
