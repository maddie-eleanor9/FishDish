import pygame


class Jellyfish:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("jellyfish.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def move(self, direction, distance):

        if direction == "right":
            self.x = self.x + distance
        elif direction == "left":
            self.x = self.x - distance
        elif direction == "up":
            self.y = self.y - distance
        elif direction == "down":
            self.y = self.y + distance
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
