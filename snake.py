import pygame

class Snake:
    def __init__(self, initial_position=(0,0), snake_size = 1, map_dimensions=()):
        self.initial_position = initial_position
        self.map_dimensions = map_dimensions

        self.position = []
        self.position.append(self.initial_position)

        for i in range(0,snake_size):
            self.position.append((self.initial_position[0] + len(self.position)*10,
                                  self.initial_position[1]))

    def update_tail(self):
        new_position = []
        new_position.append(self.position[0])
        for i in range(1,len(self.position)):
            new_position.append(self.position[i-1])
        self.position =  new_position

    def update_head(self,x=0,y=0):
        self.position[0] = ((self.position[0][0] + x) % self.map_dimensions[0],
                            (self.position[0][1] + y) % self.map_dimensions[1])

    def eat(self, x, y):
        for i in range(0,5):
            self.position = [(x,y)] + self.position

    def draw(self, screen, color):
        for i in self.position:
            pygame.draw.rect(screen, color, pygame.Rect(i[0], i[1], 10, 10))
