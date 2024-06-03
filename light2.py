import pygame


class Light2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("light_test7.png")#.convert_alpha()
        # self.image.set_alpha(75)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.7


    def move_direction(self, direction):
        if direction == "right":
            self.x = self.x + self.delta
        elif direction == "left":
            self.x = self.x - self.delta
        elif direction == "up":
            self.y = self.y - self.delta
        elif direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
