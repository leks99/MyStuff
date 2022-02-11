import pygame

class BlankObject:
    def __init__(self):
        self.ammo = 0
        self.hp = 0
        self.team = 100
        self.destroy = False
        self.size = (1, 1)
        self.position = (9999, 9999)
        self.collision = pygame.Rect(self.position, self.size)

    def draw(self, display, DEBUG):
        pass

    def update(self, allList):
        pass

    def isColliding(self, allList):
        return False

    def isOutOfMap(self):
        return False