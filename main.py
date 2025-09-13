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

    while True:
        screen.fill(color_black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                return
if __name__ == '__main__':
    main()