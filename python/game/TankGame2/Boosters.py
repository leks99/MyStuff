import pygame


class Booster:
    # ---------------20 HP booster------------------
    class HP20:
        def __init__(self, location, size):
            self.color = (0, 50, 0)
            self.team = 89
            self.destroy = False
            self.hpBoost = 20
            self.size = size
            self.location = location
            self.collision = pygame.Rect(self.location, self.size)

        def draw(self, display, DEBUG):
            pygame.draw.rect(display, self.color, self.collision)

        def update(self, allList):
            pass

        def isColliding(self, allList):
            return False

        def isOutOfMap(self):
            return False
    # ---------------40 HP booster------------------
    class HP40:
        def __init__(self, location, size):
            self.color = (0, 100, 0)
            self.team = 89
            self.destroy = False
            self.hpBoost = 40
            self.size = size
            self.location = location
            self.collision = pygame.Rect(self.location, self.size)

        def draw(self, display, DEBUG):
            pygame.draw.rect(display, self.color, self.collision)

        def update(self, allList):
            pass

        def isColliding(self, allList):
            return False

        def isOutOfMap(self):
            return False
    # ---------------2 ammo booster------------------
    class ammo2:
        def __init__(self, location, size):
            self.color = (0, 0, 50)
            self.team = 88
            self.destroy = False
            self.ammoBoost = 2
            self.size = size
            self.location = location
            self.collision = pygame.Rect(self.location, self.size)

        def draw(self, display, DEBUG):
            pygame.draw.rect(display, self.color, self.collision)

        def update(self, allList):
            pass

        def isColliding(self, allList):
            return False

        def isOutOfMap(self):
            return False
    # ---------------4 ammo booster------------------
    class ammo4:
        def __init__(self, location, size):
            self.color = (0, 0, 100)
            self.team = 88
            self.destroy = False
            self.ammoBoost = 4
            self.size = size
            self.location = location
            self.collision = pygame.Rect(self.location, self.size)

        def draw(self, display, DEBUG):
            pygame.draw.rect(display, self.color, self.collision)

        def update(self, allList):
            pass

        def isColliding(self, allList):
            return False

        def isOutOfMap(self):
            return False