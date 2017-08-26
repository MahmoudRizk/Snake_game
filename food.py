import pygame
import random

class Food:
    def __init__(self):
        self.x = 1
        self.y = 1

    def generate(self,snake_position):
        self.x = random.randint(0,390)
        self.y = random.randint(0,290)

        while self.x % 10 != 0:
            self.x = random.randint(0,390) ## TODO : update with map_dimensions
        while self.y % 10 != 0:
            self.y = random.randint(0,290) ## TODO : update with map_dimensions

        for i in snake_position:
            if i == (self.x, self.y):
                ##print "Food touches snake!!" ## Debug
                ##print i ## Debug
                self.generate(snake_position)
                break

    def draw(self,screen):
        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect(self.x, self.y, 10, 10))

    def position(self):
        return (self.x, self.y)
