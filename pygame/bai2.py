import pygame

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🏓 Pong Game")

WHITE = (255, 255, 255)
BALL_SPEED = [4, 4]

paddle_w, paddle_h = 10, 60
player1 = pygame.Rect(10, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h)
player2 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - paddle_h // 2, paddle_w, paddle_h)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

score1, score2 = 0, 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.y > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.y < HEIGHT - paddle_h:
        player1.y += 5
    if keys[pygame.K_UP] and player2.y > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.y < HEIGHT - paddle_h:
        player2.y += 5

    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

    if ball.y <= 0 or ball.y >= HEIGHT - 20:
        BALL_SPEED[1] = -BALL_SPEED[1]

    if ball.colliderect(player1) or ball.colliderect(player2):
        BALL_SPEED[0] = -BALL_SPEED[0]

    if ball.x <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    if ball.x >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
