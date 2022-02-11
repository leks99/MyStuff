import pygame
import time

class Bullet:
    def __init__(self, location, direction, speed, damage):
        self.creationDate = time.time()
        self.time = 0
        self.hp = 99999
        self.team = 99
        self.destroy = False
        self.damage = damage
        self.size = (5, 5)
        self.position = location
        self.direction = direction
        self.speed = speed
        self.velocity = tuple([i * self.speed for i in self.direction])
        self.collision = pygame.Rect(self.position, self.size)

    def draw(self, display, DEBUG):
        pygame.draw.rect(display, (150, 0, 0), self.collision)
        if DEBUG:
            print("-----------Bullet info--------------")
            print("location: ", self.position)
            print("velocity: ", self.velocity)
            print("Time: ", self.time)

    def update(self, allList):
        self.time = time.time() - self.creationDate
        if self.time > 10:
            self.destroy = True
        self.position = self.move(self.position, self.velocity)
        self.collision = pygame.Rect(self.position, self.size)
        if self.isColliding(allList)[0] or self.isOutOfMap():
            self.bounce()

    def isColliding(self, allList):
        for object in allList:
            if object.team != self.team:
                if self.collision.colliderect(object.collision):
                    if object.team == 98:
                        return [True, object]
        return [False, allList[0]]

    def isOutOfMap(self):
        if self.position[0] < 0:
            return True
        if self.position[0] + self.size[0] > 1900:
            return True
        if self.position[1] < 0:
            return True
        if self.position[1] + self.size[1] > 1000:
            return True
        else:
            return False

    def move(self, position, velocity):
        return tuple(ele1 + ele2 for ele1, ele2 in zip(position, velocity))

    def bounce(self):
        self.velocity = tuple([i * -1 for i in self.velocity])
