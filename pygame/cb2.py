import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bài tập 2 - Hình tròn di chuyển")

x, y = width // 2, height // 2
speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    
    screen.fill((0, 0, 0))  # Màu đen
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)  # Hình tròn đỏ
    pygame.display.flip()

pygame.quit()