import pygame

class Wall:
    def __init__(self, location, size, color):
        self.color = color
        self.hp = 99999
        self.team = 98
        self.destroy = False
        self.size = size
        self.position = location
        self.collision = pygame.Rect(self.position, self.size)

    def draw(self, display, DEBUG):
        pygame.draw.rect(display, self.color, self.collision)

    def update(self, allList):
        pass

    def isColliding(self, allList):
        return False

    def isOutOfMap(self):
        return False
