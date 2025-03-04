import pygame 
import random 
import time

pygame.init()
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Đuổi Bắt Đơn Giản")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

player_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

enemy_radius = 15
enemy_x = random.randint(enemy_radius, WIDTH - enemy_radius)
enemy_y = random.randint(enemy_radius, HEIGHT - enemy_radius)

lives = 3
font = pygame.font.Font(None, 36)

start_time = time.time()
running = True
Game_Over = False

while running:
    pygame.time.delay(30)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > player_radius:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < HEIGHT - player_radius:
        player_y += player_speed
    if keys[pygame.K_a] and player_x > player_radius:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < WIDTH - player_radius:
        player_x += player_speed

    if time.time() - start_time >= 2:
        enemy_x = random.randint(enemy_radius, WIDTH - enemy_radius)
        enemy_y = random.randint(enemy_radius, HEIGHT - enemy_radius)
        start_time = time.time()

    distance = ((player_x - enemy_x)**2 + (player_y - enemy_y)**2)**0.5
    if distance < player_radius + enemy_radius:
        lives -= 1
        if lives == 0:
            Game_Over = True
        else:
            enemy_x = random.randint(enemy_radius, WIDTH - enemy_radius)
            enemy_y = random.randint(enemy_radius, HEIGHT - enemy_radius)

    screen.fill(WHITE)

    if Game_Over:
        text = font.render("Game Over", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Dừng 2 giây để hiển thị thông báo
        running = False
    else:
        pygame.draw.circle(screen, GREEN, (player_x, player_y), player_radius)
        pygame.draw.circle(screen, RED, (enemy_x, enemy_y), enemy_radius)
        text = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(text, (WIDTH - text.get_width() - 100, 10))

    pygame.display.update()

pygame.quit()
