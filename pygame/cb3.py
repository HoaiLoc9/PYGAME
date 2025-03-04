import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bài tập 3 - Va chạm tường")

x, y = width // 2, height // 2
speed = 5
radius = 20
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius < width:
        x += speed
    if keys[pygame.K_UP] and y - radius > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius < height:
        y += speed
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), (x, y), radius)  # Hình tròn xanh
    pygame.display.flip()

pygame.quit()