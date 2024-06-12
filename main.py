import pygame
import random
from instructions import Instructions
from player import Player
from food import Food
from light2 import Light2
from jellyfish import Jellyfish
import time



#setup pygame
pygame.init()
pygame.font.init()
title_font = pygame.font.SysFont('Showcard Gothic', 60)
space_to_start_font = pygame.font.SysFont('Showcard Gothic', 20)
score_font = pygame.font.SysFont('Showcard Gothic', 10)
instructions_font = pygame.font.SysFont('Rockwell', 20)
pygame.display.set_caption("Fish Dish")
bg = pygame.image.load("background.png")
bg_filter = pygame.image.load("background.png")
bg_filter.set_alpha(250)

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
food_needed = 10
time_left = 45

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

instruction4 = "And watch out for jellyfish!!"
display_instruction4 = instructions_font.render(instruction4, True, (255, 255, 255))

instruction5 = "Press space to start!"
display_instruction5 = instructions_font.render(instruction5, True, (255, 255, 255))

food_needed_text = "Food Needed: "
display_food_needed = score_font.render(food_needed_text + str(food_needed), True, (255, 255, 255))

timer_text = "Time Left: "
display_timer = score_font.render(timer_text + str(time_left), True, (255, 255, 255))

lost_jellyfish_text = "Your ran into a jellyfish and lost!"
display_lost_jellyfish = space_to_start_font.render(lost_jellyfish_text, True, (255, 255, 255))

lost_food_text = "You didn't get enough food in time!"
display_lost_food = space_to_start_font.render(lost_food_text, True, (255, 255, 255))

win_text = "You Won!!"
display_win = space_to_start_font.render(win_text, True, (255, 255, 255))
print("win text: " + str(display_win.get_size()))

#making sprites
i = Instructions(195, 200)
p = Player(230, 155)
l = Light2(200, 105)
f1_x = random.randint(1,490)
f1_y = random.randint(1, 330)
f1 = Food(f1_x, f1_y)
j1_x = random.randint(1,490)
j1_y = random.randint(1,330)
j1 = Jellyfish(j1_x, j1_y)
j2_x = random.randint(1,490)
j2_y = random.randint(1,330)
j2 = Jellyfish(j2_x,j2_y)

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
        calculate_seconds = round(current_time - start_time, 2)
        time_left = round(45 - calculate_seconds, 2)
        timer_text = "Time Left: "
        display_timer = score_font.render(timer_text + str(time_left), True, (255, 255, 255))


        if calculate_seconds % 3 == 0:
            fish_move = random.randint(1,4)
            if fish_move == 1 and f1.y > 40:
                f1.move("up",50)
            elif fish_move == 2 and f1.y < 270:
                f1.move("down", 50)
            elif fish_move == 3 and f1.x > 40:
                f1.move("left", 50)
            elif fish_move == 4 and f1.x < 490:
                f1.move("right", 50)


        if calculate_seconds % 4 == 0:
            jellyfish_move = random.randint(1, 4)
            if jellyfish_move == 1 and j1.y > 100:
                j1.move("up", 70)
            elif jellyfish_move == 2 and j1.y < 430:
                j1.move("down", 70)
            elif jellyfish_move == 3 and j1.x > 100:
                j1.move("left", 70)
            elif jellyfish_move == 4 and j1.x < 490:
                j1.move("right", 70)

            jellyfish_move = random.randint(1, 4)
            if jellyfish_move == 1 and j2.y > 100:
                j2.move("up", 70)
            elif jellyfish_move == 2 and j2.y < 430:
                j2.move("down", 70)
            elif jellyfish_move == 3 and j2.x > 100:
                j2.move("left", 70)
            elif jellyfish_move == 4 and j2.x < 490:
                j2.move("right", 70)



        if time_left <= 0:
            level_1 = False
            lost_food = True


        if p.rect.colliderect(f1.rect):
            food_needed = food_needed - 1
            f1_x = random.randint(1, 490)
            f1_y = random.randint(1, 330)
            f1 = Food(f1_x, f1_y)
            display_food_needed = score_font.render(food_needed_text + str(food_needed), True, (255, 255, 255))

        if p.rect.colliderect(j1.rect) or p.rect.colliderect(j2.rect):
            level_1 = False
            lost_enemy = True


        if food_needed == 0:
            level_1 = False
            win_screen = True
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
        screen.blit(j1.image, j1.rect)
        screen.blit(j2.image, j2.rect)
        screen.blit(bg_filter, (0, 0))
        screen.blit(l.image, l.rect, special_flags=pygame.BLENDMODE_NONE)
        screen.blit(p.image, p.rect)
        screen.blit(display_food_needed, (10, 10))
        screen.blit(display_timer, (10, 30))
    elif lost_enemy == True:
        screen.blit(display_lost_jellyfish, (77, 175))
    elif lost_food == True:
        screen.blit(display_lost_food, (72, 175))
    elif win_screen == True:
        screen.blit(display_win, (209, 175))
    pygame.display.update()


pygame.quit()