import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bài tập 6 - Thu thập vật phẩm")

x, y = width // 2, height - 50
speed = 5
score = 0
font = pygame.font.Font(None, 36)

# Vật phẩm rơi
item_x = random.randint(0, width - 20)
item_y = -20
item_speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < width - 20:
        x += speed
    
    # Di chuyển vật phẩm
    item_y += item_speed
    if item_y > height:
        item_x = random.randint(0, width - 20)
        item_y = -20
    
    # Kiểm tra va chạm
    player_rect = pygame.Rect(x, y, 20, 20)
    item_rect = pygame.Rect(item_x, item_y, 20, 20)
    if player_rect.colliderect(item_rect):
        score += 10
        item_x = random.randint(0, width - 20)
        item_y = -20
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 20, 20))  # Người chơi
    pygame.draw.rect(screen, (0, 255, 0), (item_x, item_y, 20, 20))  # Vật phẩm
    score_text = font.render(f"Điểm: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()