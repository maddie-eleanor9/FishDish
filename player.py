import pygame


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player.png")
        self.image_size = self.image.get_size()
        print("player: " + str(self.image.get_size()))
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.7
        self.current_direction = "right"


    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)

        if direction == "right":
            self.x = self.x + self.delta
            self.current_direction = "right"
        elif direction == "left":
            self.x = self.x - self.delta
            self.current_direction = "left"
        elif direction == "up":
            self.y = self.y - self.delta
        elif direction == "down":
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
