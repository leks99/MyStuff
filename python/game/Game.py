import pygame
import os
import random

'''
to do list:
- make map
- display hp n bullets
- add bonuses on map
- more players
'''

# settings---------------------------------------------
WINDOW_W, WINDOW_H = 1800, 1000 # can break game (default 1800 by 1000)
BACKGROUND_COLOR = (51, 160, 51)
FPS = 30 # can break game (default 60)
STARTAMMO = 10
STARTHP = 100
PLAYERSPEED = 7
BULLETSPEED = 8
DEBUG = False
# -----------------------------------------------------

# map settings
enemyXStart = WINDOW_W - 80
enemyYStart = WINDOW_H - 80
playerXStart = 20
playerYStart = 20

pygame.init()

# other stuff
loopCounter = 0
playerX = playerXStart
playerY = playerYStart
enemyX = 500
enemyy = 800
addPlayer = True
addEnemy = True
addMap = True
tankImageScale = 0.08
tankImageDimensionX = 616 * tankImageScale
tankImageDimensionY = 692 * tankImageScale
tankImageDimensions = (int(tankImageDimensionX), int(tankImageDimensionY))
clock = pygame.time.Clock()
colorTeam0 = (0,0,255)
colorTeam1 = (255,0,0)
colorTeam2 = (0,255,0)
colorTeam3 = (0,0,0)
colorWalls = (189, 151, 13)
removeBullet = False

# events
key_w_isPressed = False
key_s_isPressed = False
key_a_isPressed = False
key_d_isPressed = False
key_space_isPressed = False
player0_shot = False

key_up_isPressed = False
key_down_isPressed = False
key_left_isPressed = False
key_right_isPressed = False
key_rshift_isPressed = False
player1_shot = False

# import tekstures
icon = pygame.image.load("playerTank.png")
playerTankImagePre = pygame.image.load("playerTank.png")
playerTankImage = pygame.transform.scale(playerTankImagePre, tankImageDimensions)
enemyTankImagePre = pygame.image.load("enemyTank.png")
enemyTankImage = pygame.transform.scale(enemyTankImagePre, tankImageDimensions)

# set up stuff
run = True
pygame.display.set_caption("czolgi:)")
pygame.display.set_icon(icon)
playerList = []
bulletList = []
mapList = []

# set up display
display = pygame.display.set_mode((WINDOW_W, WINDOW_H))

class Tank:
    def __init__(self, ammo, hitPoints, team, posX, posY, tankImage, id, isFirstStartup):
        # defining stuff
        self.isFirstStartup = isFirstStartup
        if self.isFirstStartup:
            self.isFirstStartup = False
            self.lastDir = "down"
            self.imageRaw = tankImage
            self.id = id
            self.ammo = ammo
            self.hitPoints = hitPoints
            self.team = team
            self.X = posX
            self.Y = posY
        self.isGoingUp = False
        self.isGoingDown = False
        self.isGoingLeft = False
        self.isGoingRight = False
        self.gonnaColideA = False
        self.gonnaColideD = False
        self.gonnaColideW = False
        self.gonnaColideS = False
        self.image = self.imageRaw
        self.hitbox = pygame.Rect(self.X, self.Y, tankImageDimensionX, tankImageDimensionY)

        # collision detecting
        self.hitboxA = pygame.Rect(self.X - PLAYERSPEED, self.Y, tankImageDimensionX, tankImageDimensionY)
        self.hitboxD = pygame.Rect(self.X + PLAYERSPEED, self.Y, tankImageDimensionX, tankImageDimensionY)
        self.hitboxW = pygame.Rect(self.X, self.Y - PLAYERSPEED, tankImageDimensionX, tankImageDimensionY)
        self.hitboxS = pygame.Rect(self.X, self.Y + PLAYERSPEED, tankImageDimensionX, tankImageDimensionY)
        for tank in playerList:
            if not self.id == tank.id:
                if not self.gonnaColideA:
                    self.gonnaColideA = self.hitboxA.colliderect(tank.hitbox)
                if not self.gonnaColideD:
                    self.gonnaColideD = self.hitboxD.colliderect(tank.hitbox)
                if not self.gonnaColideW:
                    self.gonnaColideW = self.hitboxW.colliderect(tank.hitbox)
                if not self.gonnaColideS:
                    self.gonnaColideS = self.hitboxS.colliderect(tank.hitbox)
        if not self.gonnaColideA:
            for map in mapList:
                for box in map.boxList:
                    if not self.gonnaColideA:
                        self.gonnaColideA = self.hitboxA.colliderect(box)
        if not self.gonnaColideD:
            for map in mapList:
                for box in map.boxList:
                    if not self.gonnaColideD:
                        self.gonnaColideD = self.hitboxD.colliderect(box)
        if not self.gonnaColideW:
            for map in mapList:
                for box in map.boxList:
                    if not self.gonnaColideW:
                        self.gonnaColideW = self.hitboxW.colliderect(box)
        if not self.gonnaColideS:
            for map in mapList:
                for box in map.boxList:
                    if not self.gonnaColideS:
                        self.gonnaColideS = self.hitboxS.colliderect(box)

        #move self
        if self.team == 0:
            if key_w_isPressed:
                if not self.gonnaColideW:
                    self.Y += -PLAYERSPEED
                    if self.Y < 0:
                        self.Y += PLAYERSPEED
                    self.lastDir = "up"
            elif key_s_isPressed:
                if not self.gonnaColideS:
                    self.Y += PLAYERSPEED
                    if self.Y > WINDOW_H - tankImageDimensionY:
                        self.Y += -PLAYERSPEED
                    self.lastDir = "down"
            elif key_a_isPressed:
                if not self.gonnaColideA:
                    self.X += -PLAYERSPEED
                    if self.X < 0:
                        self.X += PLAYERSPEED
                    self.lastDir = "left"
            elif key_d_isPressed:
                if not self.gonnaColideD:
                    self.X += PLAYERSPEED
                    if self.X > WINDOW_W - tankImageDimensionX:
                        self.X += -PLAYERSPEED
                    self.lastDir = "right"

        if self.team == 1:
            if key_up_isPressed:
                if not self.gonnaColideW:
                    self.Y += -PLAYERSPEED
                    if self.Y < 0:
                        self.Y += PLAYERSPEED
                    self.lastDir = "up"
            elif key_down_isPressed:
                if not self.gonnaColideS:
                    self.Y += PLAYERSPEED
                    if self.Y > WINDOW_H - tankImageDimensionY:
                        self.Y += -PLAYERSPEED
                    self.lastDir = "down"
            elif key_left_isPressed:
                if not self.gonnaColideA:
                    self.X += -PLAYERSPEED
                    if self.X < 0:
                        self.X += PLAYERSPEED
                    self.lastDir = "left"
            elif key_right_isPressed:
                if not self.gonnaColideD:
                    self.X += PLAYERSPEED
                    if self.X > WINDOW_W - tankImageDimensionX:
                        self.X += -PLAYERSPEED
                    self.lastDir = "right"

        # set animate events
        if self.lastDir == "up":
            self.isGoingUp = True
        elif self.lastDir == "down":
            self.isGoingDown = True
        elif self.lastDir == "left":
            self.isGoingLeft = True
        elif self.lastDir == "right":
            self.isGoingRight = True
        else:
            if loopCounter == 1:
                print("error wrong string (in set animate events)")

        # animate(rotate picture)
        if self.isGoingUp:
            self.lastDir = "up"
            self.image = self.imageRaw
        elif self.isGoingDown:
            self.lastDir = "down"
            self.image = pygame.transform.rotate(self.image, 180)
        elif self.isGoingLeft:
            self.lastDir = "left"
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.isGoingRight:
            self.lastDir = "right"
            self.image = pygame.transform.rotate(self.image, 270)

        # display self
        if self.team == 0 or self.team == 1:
            display.blit(self.image, (self.X, self.Y))
        else:
            if loopCounter == 1:
                print("error in tank class __init__ (wrong team number)", str(self.team))

        # debug in prompt
        if DEBUG:
            if loopCounter == 1:
                print("tank id:", str(self.id), "team:", str(self.team), "posX:", str(self.X), "posY:", str(self.Y),
                      "gonna colide? (a/d/w/s)", str(self.gonnaColideA), str(self.gonnaColideD), str(self.gonnaColideW),
                      str(self.gonnaColideS))

class Bullet:
    def __init__(self, id, direction, x, y, sizex, sizey, team, isFirstRun):
        self.isFirstRun = isFirstRun
        if isFirstRun:
            self.id = id
            self.direction = direction
            if direction == "up":
                self.x = x + (tankImageDimensionX // 2) -4
                self.y = y + 5
            if direction == "down":
                self.x = x + (tankImageDimensionX // 2) -4
                self.y = y + tankImageDimensionY
            if direction == "right":
                self.x = x + tankImageDimensionX
                self.y = y + (tankImageDimensionY // 2) -4
            if direction == "left":
                self.x = x
                self.y = y + (tankImageDimensionY // 2) -4
            self.isFirstRun = False
            self.sizex = sizex
            self.sizey = sizey
            self.team = team

        # move self
        if self.direction == "right":
            self.x += BULLETSPEED
        if self.direction == "left":
            self.x += -BULLETSPEED
        if self.direction == "up":
            self.y += -BULLETSPEED
        if self.direction == "down":
            self.y += BULLETSPEED

        # draw and hitbox
        self.hitbox = pygame.Rect(self.x, self.y, self.sizex, self.sizey)
        if self.team == 0:
            pygame.draw.rect(display, colorTeam0, self.hitbox)
        if self.team == 1:
            pygame.draw.rect(display, colorTeam1, self.hitbox)

        # debug in prompt
        if DEBUG:
            if loopCounter == 1:
                print("bullet id:", str(self.id), "team:", str(self.team), "posX:", str(self.x), "posY:", str(self.y))

class Maps:
    def __init__(self, isFirstRun):
        self.isFirstRun = isFirstRun
        if isFirstRun:
            self.boxList = []
            self.box1 = pygame.Rect(90, 0, 50, 400)
            self.boxList.append(self.box1)
            self.box2 = pygame.Rect(1600, 500, 50, 500)
            self.boxList.append(self.box2)
            self.box3 = pygame.Rect(90, 490, 50, 410)
            self.boxList.append(self.box3)
            self.box4 = pygame.Rect(140, 850, 500, 50)
            self.boxList.append(self.box4)
            self.isFirstRun = False

        for box in self.boxList:
            pygame.draw.rect(display, colorWalls, box)


# game loop----------------------------------------------------------------------------------------
while run:
    if DEBUG:
        if loopCounter == 1:
            print("----------------------------------------------------------------")

    loopCounter += 1
    if loopCounter == 200:
        loopCounter = 0

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            # player
            if event.key == pygame.K_w:
                key_w_isPressed = True
            if event.key == pygame.K_s:
                key_s_isPressed = True
            if event.key == pygame.K_a:
                key_a_isPressed = True
            if event.key == pygame.K_d:
                key_d_isPressed = True
            if event.key == pygame.K_SPACE:
                key_space_isPressed = True
                player0_shot = True
            # enemy
            if event.key == pygame.K_UP:
                key_up_isPressed = True
            if event.key == pygame.K_DOWN:
                key_down_isPressed = True
            if event.key == pygame.K_LEFT:
                key_left_isPressed = True
            if event.key == pygame.K_RIGHT:
                key_right_isPressed = True
            if event.key == pygame.K_RSHIFT:
                key_rshift_isPressed = True
                player1_shot = True

        if event.type == pygame.KEYUP:
            # player
            if event.key == pygame.K_w:
                key_w_isPressed = False
            if event.key == pygame.K_s:
                key_s_isPressed = False
            if event.key == pygame.K_a:
                key_a_isPressed = False
            if event.key == pygame.K_d:
                key_d_isPressed = False
            if event.key == pygame.K_SPACE:
                key_space_isPressed = False
                player0_shot = False
            # enemy
            if event.key == pygame.K_UP:
                key_up_isPressed = False
            if event.key == pygame.K_DOWN:
                key_down_isPressed = False
            if event.key == pygame.K_LEFT:
                key_left_isPressed = False
            if event.key == pygame.K_RIGHT:
                key_right_isPressed = False
            if event.key == pygame.K_RSHIFT:
                key_rshift_isPressed = False
                player1_shot = False

    display.fill(BACKGROUND_COLOR)

    # add player (to list)
    if addPlayer:
        playerList.append(Tank(STARTAMMO, STARTHP, 0, playerX, playerY, playerTankImage, 0, True))
        addPlayer = False

    # add enemy (to list)
    if addEnemy:
        playerList.append(Tank(STARTAMMO, STARTHP, 1, enemyXStart, enemyYStart, enemyTankImage, 1, True))
        addEnemy = False

    # add map
    if addMap:
        mapList.append(Maps(True))

    # update maps
    for map in mapList:
        map.__init__(map.isFirstRun)

    # add bullet (to list)
    bulletCounter = 0
    for bullet in bulletList:
        bulletCounter += 1

    # update tanks
    for tank in playerList:
        tank.__init__(tank.ammo, tank.hitPoints, tank.team, tank.X, tank.Y, tank.imageRaw, tank.id, tank.isFirstStartup)
        if key_space_isPressed and tank.team == 0 and player0_shot and tank.ammo > 0:
            bulletList.append(Bullet(bulletCounter, tank.lastDir, tank.X, tank.Y, 10, 10, 0, True))
            player0_shot = False
            tank.ammo += -1
        if key_rshift_isPressed and tank.team == 1 and player1_shot and tank.ammo > 0:
            bulletList.append(Bullet(bulletCounter, tank.lastDir, tank.X, tank.Y, 10, 10, 1, True))
            player1_shot = False
            tank.ammo += -1

    #update bullets
    for bullet in bulletList:
        removeBullet = False
        bullet.__init__(bullet.id, bullet.direction, bullet.x, bullet.y, bullet.sizex, bullet.sizey, bullet.team, bullet.isFirstRun)
        if bullet.x > WINDOW_W or bullet.x < 0 or bullet.y > WINDOW_H or bullet.y < 0:
            removeBullet = True
        for map in mapList:
            for box in map.boxList:
                if bullet.hitbox.colliderect(box):
                    removeBullet = True
        for tank in playerList:
            if bullet.hitbox.colliderect(tank.hitbox):
                tank.hitPoints += -20
                removeBullet = True
                if tank.hitPoints <= 0:
                    playerList.remove(tank)
        if removeBullet:
            bulletList.remove(bullet)


    pygame.display.update()
    if DEBUG:
        if loopCounter == 1:
            print("----------------------------------------------------------------")

# end of game loop---------------------------------------------------------------------------------

pygame.quit()

# case imported
if __name__ == "__main__":
    main()