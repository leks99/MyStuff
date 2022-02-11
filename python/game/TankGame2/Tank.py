import pygame
from Bullet import *

class Tank:
    def __init__(self, image, imageDimensions, team, hp, ammo, position):
        self.bulletDamage = 20
        self.destroy = False
        self.imageDimensions = imageDimensions
        self.image = image
        self.imageRaw = image
        self.team = team
        self.hp = hp
        self.ammo = ammo
        self.position = position
        self.lastPosition = position
        self.speed = 4
        self.direction = (0, 1)
        self.bulletSpeed = 6
        self.collision = pygame.Rect(self.position[0], self.position[1], self.imageDimensions[0], self.imageDimensions[1])

    def draw(self, display, DEBUG):
        display.blit(self.image, self.position)
        if DEBUG == True:
            print("-----------Tank info------------")
            print("Team: ", self.team)
            print("HP = ", self.hp)
            print("Rect pos: ", self.collision.x, " ", self.collision.y)
            print("Tank pos: ", self.position)
            print("Destroy = ", self.destroy)
            print("Out of map = ", self.isOutOfMap())

    def goUp(self, allList):
        self.position = self.position[0], self.position[1] - self.speed
        self.collision = pygame.Rect(self.position, self.imageDimensions)
        if self.isColliding(allList)[0] or self.isOutOfMap():
            self.position = self.lastPosition
        else:
            self.lastPosition = self.position
        self.image = pygame.transform.rotate(self.imageRaw, 0)
        self.direction = (0, -1)

    def goDown(self, allList):
        self.position = self.position[0], self.position[1] + self.speed
        self.collision = pygame.Rect(self.position, self.imageDimensions)
        if self.isColliding(allList)[0] or self.isOutOfMap():
            self.position = self.lastPosition
        else:
            self.lastPosition = self.position
        self.image = pygame.transform.rotate(self.imageRaw, 180)
        self.direction = (0, 1)

    def goLeft(self, allList):
        self.position = self.position[0] - self.speed, self.position[1]
        self.collision = pygame.Rect(self.position, self.imageDimensions)
        if self.isColliding(allList)[0] or self.isOutOfMap():
            self.position = self.lastPosition
        else:
            self.lastPosition = self.position
        self.image = pygame.transform.rotate(self.imageRaw, 90)
        self.direction = (-1, 0)

    def goRight(self, allList):
        self.position = self.position[0] + self.speed, self.position[1]
        self.collision = pygame.Rect(self.position, self.imageDimensions)
        if self.isColliding(allList)[0] or self.isOutOfMap():
            self.position = self.lastPosition
        else:
            self.lastPosition = self.position
        self.image = pygame.transform.rotate(self.imageRaw, 270)
        self.direction = (1, 0)

    def shoot(self, allList):
        if self.direction == (0, -1) and self.ammo > 0: #  UP
            bPos = ((self.position[0] - 2 + self.imageDimensions[0]/2), (self.position[1]-5))
            allList.append(Bullet(bPos, self.direction, self.bulletSpeed, self.bulletDamage))
            self.ammo -= 1
        if self.direction == (0, 1) and self.ammo > 0: #  DOWN
            bPos = ((self.position[0] - 2 + self.imageDimensions[0]/2), (self.position[1] + self.imageDimensions[1]+1))
            allList.append(Bullet(bPos, self.direction, self.bulletSpeed, self.bulletDamage))
            self.ammo -= 1
        if self.direction == (-1, 0) and self.ammo > 0: #  LEFT
            bPos = ((self.position[0]-5), (self.position[1] - 5 + self.imageDimensions[1]/2))
            allList.append(Bullet(bPos, self.direction, self.bulletSpeed, self.bulletDamage))
            self.ammo -= 1
        if self.direction == (1, 0) and self.ammo > 0: #  RIGHT
            bPos = ((self.position[0] + self.imageDimensions[0]+1), (self.position[1] - 5 + self.imageDimensions[1]/2))
            allList.append(Bullet(bPos, self.direction, self.bulletSpeed, self.bulletDamage))
            self.ammo -= 1

    def update(self, allList):
        if self.hp <= 0:
            self.destroy = True
        self.collide(allList)

    def isColliding(self, allList):
        for object in allList:
            if object.team != self.team:
                if self.collision.colliderect(object.collision):
                    return [True, object]
        return [False, allList[0]]

    def collide(self, allList):
        for object in allList:
            if object.team != self.team:
                if self.collision.colliderect(object.collision):
                    if object.team == 99:
                        self.hp -= object.damage
                        object.destroy = True
                    elif object.team == 89:
                        self.hp += object.hpBoost
                        object.destroy = True
                    elif object.team == 88:
                        self.ammo += object.ammoBoost
                        object.destroy = True
                    return True
        return False

    def isOutOfMap(self):
        if self.position[0] < 0:
            return True
        if self.position[0] + self.imageDimensions[0] > 1900:
            return True
        if self.position[1] < 0:
            return True
        if self.position[1] + self.imageDimensions[1] > 1000:
            return True
        else:
            return False
