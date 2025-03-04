import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bài tập 4 - Thêm hình ảnh")

# Tải hình ảnh (thay bằng đường dẫn tới hình ảnh của bạn)
image = pygame.image.load("player.png").convert_alpha()
image = pygame.transform.scale(image, (50, 50))  # Thay đổi kích thước nếu cần
x, y = width // 2, height // 2
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < width - 50:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < height - 50:
        y += speed
    
    screen.fill((255, 255, 255))
    screen.blit(image, (x, y))  # Vẽ hình ảnh
    pygame.display.flip()

pygame.quit()