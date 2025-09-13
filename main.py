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
        pygame.draw.rect(screen, color_white, paddle_1_rect)
        pygame.draw.rect(screen, color_white, paddle_2_rect)
        pygame.draw.rect(screen, color_white, ball_rect)
        pygame.display.update()
        delta_time = clock.tick(60)
        
if __name__ == '__main__':
    main()