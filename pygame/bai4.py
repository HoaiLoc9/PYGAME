import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Mario Style 🏃‍♂️")

# Tải hình ảnh
player_img = pygame.image.load("assets/mario.png")
player_img = pygame.transform.scale(player_img, (40, 50))
enemy_img = pygame.image.load("assets/enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (40, 50))
coin_img = pygame.image.load("assets/coin.png")
coin_img = pygame.transform.scale(coin_img, (20, 20))
bg_img = pygame.image.load("assets/background.png")

# Âm thanh
jump_sound = pygame.mixer.Sound("assets/jump.wav")
coin_sound = pygame.mixer.Sound("assets/coin.wav")
hit_sound = pygame.mixer.Sound("assets/hit.wav")

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Nhân vật
player_size = (40, 50)
player = pygame.Rect(50, HEIGHT - 100, *player_size)
player_speed = 5
gravity = 0.5
jump_power = -10
velocity_y = 0

# Nền tảng
platforms = [pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
             pygame.Rect(200, 350, 100, 10),
             pygame.Rect(400, 250, 100, 10),
             pygame.Rect(600, 150, 100, 10)]

# Đồng xu
coin = pygame.Rect(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 150), 20, 20)
score = 0

# Quái vật
enemy = pygame.Rect(600, HEIGHT - 90, 40, 50)
enemy_speed = 2

# Thanh máu
health = 3

# Font chữ
font = pygame.font.Font(None, 36)

# Vòng lặp game
clock = pygame.time.Clock()
running = True
on_ground = False

while running:
    screen.fill(WHITE)
    screen.blit(bg_img, (0, 0))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Điều khiển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power
        jump_sound.play()

    # Cập nhật vị trí nhân vật
    velocity_y += gravity
    player.y += velocity_y

    # Kiểm tra va chạm với nền tảng
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform) and velocity_y > 0:
            player.y = platform.y - player_size[1]
            velocity_y = 0
            on_ground = True

    # Nhặt đồng xu
    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(100, WIDTH - 100)
        coin.y = random.randint(100, HEIGHT - 150)
        coin_sound.play()

    # Di chuyển quái vật
    enemy.x += enemy_speed
    if enemy.x <= 0 or enemy.x >= WIDTH - 40:
        enemy_speed = -enemy_speed

    # Kiểm tra va chạm với quái vật
    if player.colliderect(enemy):
        health -= 1
        hit_sound.play()
        player.x = 50  # Đưa nhân vật về đầu màn
        player.y = HEIGHT - 100

    # Kiểm tra thua cuộc
    if health <= 0:
        screen.fill((0, 0, 0))
        text = font.render("Game Over! Nhấn R để chơi lại", True, (255, 0, 0))
        screen.blit(text, (WIDTH // 6, HEIGHT // 3))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    # Vẽ nhân vật
    screen.blit(player_img, (player.x, player.y))
    
    # Vẽ quái vật
    screen.blit(enemy_img, (enemy.x, enemy.y))

    # Vẽ nền tảng
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    # Vẽ đồng xu
    screen.blit(coin_img, (coin.x, coin.y))

    # Hiển thị điểm số
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Hiển thị máu
    health_text = font.render(f"Health: {health}", True, (255, 0, 0))
    screen.blit(health_text, (10, 40))

    # Cập nhật màn hình
    pygame.display.update()
    clock.tick(30)

pygame.quit()
