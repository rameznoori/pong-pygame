import pygame
import random

screen_height = 720
screen_width = 960

color_black = (0,0,0)
color_white = (255,255,255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong")

    paddle_1_rect = pygame.Rect(30,0,7,100)
    paddle_2_rect = pygame.Rect(screen_width - 50,0,7,100)
    paddle_1_move = 0
    paddle_2_move = 0
    ball_rect = pygame.Rect(screen_width/2, screen_height/2, 25,25)
    ball_accel_x = random.randint(2,4)*0.1
    ball_accel_y = random.randint(2,4)*0.1

    if random.randint(1,2) == 1:
        ball_accel_x *= -1
    if random.randint(1,2) == 1:
        ball_accel_y *= -1

    clock = pygame.time.Clock()
    started = False

    while True:
        screen.fill(color_black)
        if not started:
            font = pygame.font.SysFont('Consolas', 30)
            text = font.render('Press Space to Start', True, color_white)
            text_rect = text.get_rect()
            text_rect.center = (screen_width//2, screen_height//2)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1_move = 0.0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2_move = 0.0
        if ball_rect.left <=0 or ball_rect.left >= screen_width:
            return
        if ball_rect.top <0:
            ball_accel_y *= -1
            ball_rect.top = 0
        if ball_rect.bottom > screen_height - ball_rect.height:
            ball_accel_y *= -1
            ball_rect.top = screen_height - ball_rect.height
        if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left += 5
        if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.left > ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left -= 5
        if started:
            ball_rect.left += ball_accel_x * delta_time
            ball_rect.top += ball_accel_y * delta_time
        pygame.draw.rect(screen, color_white, paddle_1_rect)
        pygame.draw.rect(screen, color_white, paddle_2_rect)
        pygame.draw.rect(screen, color_white, ball_rect)
        pygame.display.update()
        delta_time = clock.tick(60) 
        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time
        
if __name__ == '__main__':
    main()