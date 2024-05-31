import pygame


class Food:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("food.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.current_direction = "left"
        self.delta = 0.8
        self.moved = 0


    def move(self, direction, distance):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)


        if direction == "right":
            while self.moved < distance:
                self.x = self.x + self.delta
                self.moved = self.moved + self.delta
            self.moved = 0
            self.current_direction = "right"
        elif direction == "left":
            while self.moved < distance:
                self.x = self.x - self.delta
                self.moved = self.moved + self.delta
            self.moved = 0
            self.current_direction = "left"
        elif direction == "up":
            self.y = self.y - distance
        elif direction == "down":
            self.y = self.y + distance
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
