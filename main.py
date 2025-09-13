import pygame
import random

screen_height = 720
screen_width = 960

color_black = (0,0,0)
color_white = (255,255,255)
color_red = (255, 0, 0)
color_green = (00,255,00)
color_blue = (167,199,231)

def reset_game():
    paddle_1_rect = pygame.Rect(30, 0, 7, 100)
    paddle_2_rect = pygame.Rect(screen_width - 50, 0, 7, 100)
    ball_rect = pygame.Rect(int(screen_width/2), int(screen_height/2), 25, 25)
    ball_accel_x = random.randint(2,4)*0.1
    ball_accel_y = random.randint(2,4)*0.1

    if random.randint(1,2) == 1:
        ball_accel_x *= -1
    if random.randint(1,2) == 1:
        ball_accel_y *= -1

    return paddle_1_rect, paddle_2_rect, ball_rect, ball_accel_x, ball_accel_y

def draw_dotted_line(screen, color, x, y_start, y_end, dash_length=10, gap_length=10):
    y = y_start
    while y <y_end:
        pygame.draw.line(screen, color, (x,y), (x,min(y + dash_length, y_end)))
        y += dash_length + gap_length

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong")
    font = pygame.font.SysFont('Consolas', 30)
    score_font = pygame.font.SysFont('Consolas', 40)
    game_over_font = pygame.font.SysFont('Consolas', 50)
    win_font = pygame.font.SysFont('Consolas', 60)

    paddle_1_move = 0
    paddle_2_move = 0
    clock = pygame.time.Clock()
    started = False
    game_over = False

    score_p1 = 0
    score_p2 = 0

    paddle_1_rect, paddle_2_rect, ball_rect, ball_accel_x, ball_accel_y = reset_game()

    while True:
        delta_time = clock.tick(60)
        screen.fill(color_black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        paddle_1_rect, paddle_2_rect, ball_rect, ball_accel_x, ball_accel_y = reset_game()
                        game_over = False
                        started = False
                        paddle_1_move = paddle_2_move = 0
                        score_p1 = 0
                        score_p2 = 0
                    elif not started:
                        started = True
                if not game_over and started:
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

        if not started and not game_over:
            text = font.render('Press Space to Start', True, color_white)
            text_rect = text.get_rect()
            text_rect.center = (screen_width//2, screen_height//2)
            screen.blit(text, text_rect)
            pygame.display.flip()
            continue

        if game_over:
            text = game_over_font.render('Game Over', True, color_red)
            text_rect = text.get_rect()
            text_rect.center =  (screen_width//2, screen_height//2 - 60)
            screen.blit(text, text_rect)
            
            score_text = score_font.render(f"Player 1: {score_p1}  Player 2: {score_p2}", True, color_white)
            score_rect = score_text.get_rect()
            score_rect.center = (screen_width // 2, screen_height // 2 )
            screen.blit(score_text, score_rect)

            if score_p1 > score_p2:
                winner_text = win_font.render("Player 1 Wins!", True, color_green)
            elif score_p2 > score_p1:
                winner_text = win_font.render("Player 2 Wins!", True, color_green)
            else:
                winner_text = win_font.render("It's a Tie!", True, color_green)
            winner_rect = winner_text.get_rect()
            winner_rect.center = (screen_width // 2, screen_height // 2+140)
            screen.blit(winner_text, winner_rect)
            
            hint = font.render('Press Space to Replay', True, color_blue)
            hint_rect = hint.get_rect()
            hint_rect.center = (screen_width//2, screen_height//2 + 70)
            screen.blit(hint, hint_rect)
            pygame.display.flip()
            continue
        
        if ball_rect.left <= 0:
            score_p2 +=1
            game_over = True
            started = False
        if ball_rect.right >= screen_width:
            score_p1 +=1
            game_over =True
            started = False

        if ball_rect.top <0:
            ball_accel_y *= -1
            ball_rect.top = 0
        if ball_rect.bottom > screen_height:
            ball_accel_y *= -1
            ball_rect.bottom = screen_height
        
        if paddle_1_rect.colliderect(ball_rect) and paddle_1_rect.left < ball_rect.left:
            ball_accel_x *= -1
            ball_rect.left += 5
            score_p1 += 1
        if paddle_2_rect.colliderect(ball_rect) and paddle_2_rect.right > ball_rect.right:
            ball_accel_x *= -1
            ball_rect.left -= 5
            score_p2 += 1
        
        ball_rect.left += int(ball_accel_x * delta_time)
        ball_rect.top += int(ball_accel_y * delta_time)
        
        paddle_1_rect.top += paddle_1_move * delta_time
        paddle_2_rect.top += paddle_2_move * delta_time
        
        if paddle_1_rect.top < 0:
            paddle_1_rect.top = 0
        if paddle_1_rect.bottom > screen_height:
            paddle_1_rect.bottom = screen_height
        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > screen_height:
            paddle_2_rect.bottom = screen_height

        draw_dotted_line(screen, color_white, screen_width // 2,0,screen_height, dash_length=15, gap_length=10)  

        pygame.draw.rect(screen, color_white, paddle_1_rect)
        pygame.draw.rect(screen, color_white, paddle_2_rect)
        pygame.draw.rect(screen, color_red, ball_rect)

        player1_name = font.render("Player 1", True, color_white)
        player1_name_rect = player1_name.get_rect(midtop=(screen_width // 4,0))
        screen.blit(player1_name, player1_name_rect)

        player2_name = font.render("Player 2", True, color_white)
        player2_name_rect = player2_name.get_rect(midtop=(3* screen_width // 4,0))
        screen.blit(player2_name, player2_name_rect)

        score_p1_text = font.render("Score: "+str(score_p1), True, color_white)
        score_p1_rect = score_p1_text.get_rect(midtop=(screen_width // 4, 40))
        screen.blit(score_p1_text, score_p1_rect)

        score_p2_text = font.render("Score: "+str(score_p2), True, color_white)
        score_p2_rect = score_p2_text.get_rect(midtop=(3 * screen_width // 4, 40))
        screen.blit(score_p2_text, score_p2_rect)

        pygame.display.update() 
        
if __name__ == '__main__':
    main()