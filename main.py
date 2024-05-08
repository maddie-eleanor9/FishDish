import pygame
import random
from instructions import Instructions

#setup pygame
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Showcard Gothic', 60)
pygame.display.set_caption("Fish Dish")

#setup screen
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

#different screens
start_screen = True
level_1 = False
level_2 = False
win_screen = False
lost_food = False
lost_enemy = False

#misc variables
r = 24
g = 56
b = 99

#rendering text
title = "Fish Dish"
display_title = title_font.render(title, True, (255, 255, 255))
print(display_title.get_size())

#making sprites
i = Instructions(195, 200)
print(i.image_size)

run = True
#main program loop
while run:

    #event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP and start_screen == True:
            start_screen = False
            level_1 = True

    #blit sprites
    screen.fill((r, g, b))
    if start_screen == True:
        screen.blit(display_title, (122, 120))
        screen.blit(i.image, i.rect)
    elif level_1 == True:
        screen.fill((255, 0 ,0))
    pygame.display.update()


pygame.quit()