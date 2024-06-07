import pygame
import random
from instructions import Instructions
from player import Player
from food import Food
from light2 import Light2
import time



#setup pygame
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Showcard Gothic', 60)
space_to_start_font = pygame.font.SysFont('Showcard Gothic', 20)
instructions_font = pygame.font.SysFont('Rockwell', 20)
pygame.display.set_caption("Fish Dish")
bg = pygame.image.load("background.png")
bg_filter = pygame.image.load("background.png")
bg_filter.set_alpha(230)

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
mouse_x = 0
mouse_y = 0
coordinates = (mouse_x, mouse_y)
points = 0

#rendering text
title = "Fish Dish"
display_title = title_font.render(title, True, (255, 255, 255))

space_to_start = "Click space to start!"
display_space_to_start = space_to_start_font.render(space_to_start, True, (255, 255, 255))


instruction1 = "Use WASD to move"
display_instruction1 = instructions_font.render(instruction1, True, (255, 255, 255))

instruction2 = "Try to collect enough food for the day"
display_instruction2 = instructions_font.render(instruction2, True, (255, 255, 255))

instruction3 = "Pay attention to the timer"
display_instruction3 = instructions_font.render(instruction3, True, (255, 255, 255))

instruction4 = "And watch out for sharks and any bigger fish!!"
display_instruction4 = instructions_font.render(instruction4, True, (255, 255, 255))

instruction5 = "Press space to start!"
display_instruction5 = instructions_font.render(instruction5, True, (255, 255, 255))


#making sprites
i = Instructions(195, 200)
p = Player(230, 155)
l = Light2(200, 125)
f1_x = random.randint(1,490)
f1_y = random.randint(1, 330)
f1 = Food(f1_x, f1_y)

run = True
#main program loop
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_direction("right")
        l.move_direction("right")
    elif keys[pygame.K_a]:
        p.move_direction("left")
        l.move_direction("left")
    elif keys[pygame.K_w]:
        p.move_direction("up")
        l.move_direction("up")
    elif keys[pygame.K_s]:
        p.move_direction("down")
        l.move_direction("down")

    if level_1 == True:
        current_time = time.time()
        if current_time == start_time + 3:
            print("up")
            f1.move("up",5)
        if current_time % 5 == 0:
            print("down")
            f1.move("down", 5)

        if p.rect.colliderect(f1.rect):
            print("collided")
            points = points + 1
            f1 = Food(1000, 1000)

    #event loop
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and (start_screen == True or instructions_screen == True):
            if event.key == pygame.K_SPACE:
                start_screen = False
                instructions_screen = False
                level_1 = True
                current_time = time.time()
                start_time = current_time
                print("start time: " + str(start_time))
                print("current_time: " + str(current_time))

        if event.type == pygame.MOUSEBUTTONUP and start_screen == True:
            if i.rect.collidepoint(event.pos):
                start_screen = False
                instructions_screen = True
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            coordinates = (mouse_x, mouse_y)


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
        screen.blit(bg, (0, 0))
        screen.blit(f1.image, f1.rect)
        screen.blit(bg_filter, (0, 0))
        screen.blit(l.image, l.rect, special_flags=pygame.BLEND_RGB_ADD)
        screen.blit(p.image, p.rect)

    pygame.display.update()


pygame.quit()