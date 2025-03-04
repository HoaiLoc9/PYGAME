import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bài tập 5 - Điểm số")

x, y = width // 2, height // 2
speed = 5
score = 0
font = pygame.font.Font(None, 36)  # Font mặc định, kích thước 36

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        score += 1
    if keys[pygame.K_RIGHT] and x < width - 20:
        x += speed
        score += 1
    if keys[pygame.K_UP] and y > 0:
        y -= speed
        score += 1
    if keys[pygame.K_DOWN] and y < height - 20:
        y += speed
        score += 1
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 20)  # Hình tròn xanh dương
    score_text = font.render(f"Điểm: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))  # Hiển thị điểm ở góc trên trái
    pygame.display.flip()

pygame.quit()