import pygame
import random
from instructions import Instructions

#setup pygame
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Showcard Gothic', 60)
space_to_start_font = pygame.font.SysFont('Showcard Gothic', 20)
instructions_font = pygame.font.SysFont('Rockwell', 20)
pygame.display.set_caption("Fish Dish")

#setup screen
SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

#different screens
start_screen = True
instructions_screen = False
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

space_to_start = "Click space to start!"
display_space_to_start = space_to_start_font.render(space_to_start, True, (255, 255, 255))


instruction1 = "Use WASD to move"
display_instruction1 = instructions_font.render(instruction1, True, (255, 255, 255))
print(display_instruction1.get_size())

instruction2 = "Try to collect enough food for the day"
display_instruction2 = instructions_font.render(instruction2, True, (255, 255, 255))
print(display_instruction2.get_size())

instruction3 = "Pay attention to the timer"
display_instruction3 = instructions_font.render(instruction3, True, (255, 255, 255))
print(display_instruction3.get_size())

instruction4 = "And watch out for sharks and any bigger fish!!"
display_instruction4 = instructions_font.render(instruction4, True, (255, 255, 255))
print(display_instruction4.get_size())

instruction5 = "Press space to start!"
display_instruction5 = instructions_font.render(instruction5, True, (255, 255, 255))
print(display_instruction5.get_size())
#making sprites
i = Instructions(195, 200)

run = True
#main program loop
while run:

    #event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and (start_screen == True or instructions_screen == True):
            if event.key == pygame.K_SPACE:
                start_screen = False
                instructions_screen = False
                level_1 = True

        if event.type == pygame.MOUSEBUTTONUP and start_screen == True:
            if i.rect.collidepoint(event.pos):
                start_screen = False
                instructions_screen = True
    #blit sprites
    screen.fill((r, g, b))
    if start_screen == True:
        screen.blit(display_title, (122, 120))
        screen.blit(display_space_to_start, (152, 275))
        screen.blit(i.image, i.rect)

    elif instructions_screen == True:
        screen.blit(display_instruction1, (179, 100))
        screen.blit(display_instruction2, (90, 135))
        screen.blit(display_instruction3, (153, 170))
        screen.blit(display_instruction4, (56, 205))
        screen.blit(display_instruction5, (176, 240))
    elif level_1 == True:
        screen.fill((255, 0, 0))
    pygame.display.update()


pygame.quit()