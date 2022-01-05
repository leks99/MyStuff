import pygame as pg
import pymunk as pm
import time

"""
notes!
mass set by cubic meter

to do:
-
"""

# settings -------------------------------------------------------------------------------------------------------------
settings_fullscreen = True # default true
settings_resolution = (1900, 1000)
settings_fps = 60 # default 60
# ----------------------------------------------------------------------------------------------------------------------

# set up stuff
WHITE = (255, 255, 255) # basic stuff ----
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREY = (117, 117, 117)
SANDCOLOR = (186, 151, 56)
STONECOLOR = (90, 90, 90)
fps = settings_fps
winXY = settings_resolution
resolution = (1920, 1080)
mousexy = (0, 0)
if settings_fullscreen == True: # for pygame and time ----
    winXY = (0, 0)
    display = pg.display.set_mode(winXY, pg.FULLSCREEN)
else:
    display = pg.display.set_mode(winXY)
lastTime = time.time()
clock = pg.time.Clock()
space = pm.Space() # for pymunk ----
space.gravity = (0, 100)
weightMultiplier = 0.5
sandMass = 1600 * weightMultiplier
sandFriction = 0.4
stoneMass = 1800 * weightMultiplier
stoneFriction = 0.4
waterMass = 1000 * weightMultiplier
waterFriction = 0
super_stoneMass = 5000 * weightMultiplier
super_stoneFriction = 0.1

# lists
physicalObiectList = []
wallList = []

# events
run = True
spawn = False
spawnSand = False
spawnStone = False
spawnWater = False
spawnSuper_stone = False
addWalls = True
onePressed = False
twoPressed = False
threePressed = False
fourPressed = False

# functions -----------------------------------------------------------

# end functions -------------------------------------------------------

# class ---------------------------------------------------------------
class wall:
    def __init__(self, space, xy, sizexy):
        self.x = xy[0]
        self.y = xy[1]
        self.sizex = sizexy[0]
        self.sizey = sizexy[1]
        self.body = pm.Body(1, 100, body_type=pm.Body.STATIC)
        self.body.position = (self.x + (self.sizex // 2), self.y + (self.sizey // 2))
        self.shape = pm.Poly.create_box(self.body, size=(self.sizex, self.sizey))
        self.radius = 0
        self.rect = pg.Rect(xy[0], xy[1], self.sizex, self.sizey)
        self.shape.friction = 0.5
        space.add(self.body, self.shape)
    def update(self):
        pg.draw.rect(display, GREY, self.rect)
class sand:
    def __init__(self, space, xy):
        self.color = SANDCOLOR
        self.x = xy[0]
        self.y = xy[1]
        self.radius = 1
        self.sizexy = (1, 1)
        self.moment = pm.moment_for_box(sandMass, size=self.sizexy)
        self.body = pm.Body(sandMass, self.moment, body_type = pm.Body.DYNAMIC)
        self.body.position = xy
        self.shape = pm.Poly.create_box(self.body, size=self.sizexy)
        self.shape.friction = sandFriction
        space.add(self.body, self.shape)
    def update(self):
        xy = self.body.position
        pg.draw.circle(display, self.color, xy, self.radius)
class stone:
    def __init__(self, space, xy):
        self.color = STONECOLOR
        self.x = xy[0]
        self.y = xy[1]
        self.radius = 1
        self.sizexy = (1, 1)
        self.moment = pm.moment_for_box(stoneMass, size=self.sizexy)
        self.body = pm.Body(stoneMass, self.moment, body_type = pm.Body.DYNAMIC)
        self.body.position = xy
        self.shape = pm.Poly.create_box(self.body, size=self.sizexy)
        self.shape.friction = stoneFriction
        space.add(self.body, self.shape)
    def update(self):
        xy = self.body.position
        pg.draw.circle(display, self.color, xy, self.radius)
class water:
    def __init__(self, space, xy):
        self.color = BLUE
        self.x = xy[0]
        self.y = xy[1]
        self.radius = 1
        self.sizexy = (1, 1)
        self.moment = pm.moment_for_box(waterMass, size=self.sizexy)
        self.body = pm.Body(waterMass, self.moment, body_type = pm.Body.DYNAMIC)
        self.body.position = xy
        self.shape = pm.Poly.create_box(self.body, size=self.sizexy)
        self.shape.friction = waterFriction
        space.add(self.body, self.shape)
    def update(self):
        xy = self.body.position
        pg.draw.circle(display, self.color, xy, self.radius)
class super_stone:
    def __init__(self, space, xy):
        self.color = GREEN
        self.x = xy[0]
        self.y = xy[1]
        self.radius = 1
        self.sizexy = (1, 1)
        self.moment = pm.moment_for_box(super_stoneMass, size=self.sizexy)
        self.body = pm.Body(super_stoneMass, self.moment, body_type = pm.Body.DYNAMIC)
        self.body.position = xy
        self.shape = pm.Poly.create_box(self.body, size=self.sizexy)
        self.shape.friction = super_stoneFriction
        space.add(self.body, self.shape)
    def update(self):
        xy = self.body.position
        pg.draw.circle(display, self.color, xy, self.radius)
# end class -----------------------------------------------------------

# main loop start ------------------------------------------------------------------------------------------------------
while run:
    clock.tick(fps)
    dt = time.time() - lastTime
    lastTime = time.time()
    space.step(dt)

    display.fill(BLACK)

    # spawn
    if addWalls:
        wallList.append(wall(space, (0, resolution[1] - 25), (resolution[0], 25)))
        wallList.append(wall(space, (0, 0), (25, resolution[1] - 25)))
        wallList.append(wall(space, (resolution[0] - 25, 0), (25, resolution[1] - 25)))
        addWalls = False
    if spawn:
        if spawnSand:
            physicalObiectList.append(sand(space, (pg.mouse.get_pos())))
        if spawnStone:
            physicalObiectList.append(stone(space, (pg.mouse.get_pos())))
        if spawnWater:
            physicalObiectList.append(water(space, (pg.mouse.get_pos())))
        if spawnSuper_stone:
            physicalObiectList.append(super_stone(space, (pg.mouse.get_pos())))

    # events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DELETE:
                run = False
            if event.key == pg.K_1:
                onePressed = True
                spawnSand = True
                spawnStone = False
                spawnWater = False
                spawnSuper_stone = False
            if event.key == pg.K_2:
                twoPressed = True
                spawnSand = False
                spawnStone = True
                spawnWater = False
                spawnSuper_stone = False
            if event.key == pg.K_3:
                threePressed = True
                spawnSand = False
                spawnStone = False
                spawnWater = True
                spawnSuper_stone = False
            if event.key == pg.K_4:
                fourPressed = True
                spawnSand = False
                spawnStone = False
                spawnWater = False
                spawnSuper_stone = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_1:
                onePressed = False
            if event.key == pg.K_2:
                twoPressed = False
            if event.key == pg.K_3:
                threePressed = False
            if event.key == pg.K_4:
                fourPressed = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                spawn = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == pg.BUTTON_LEFT:
                spawn = False

    for particle in physicalObiectList:
        particle.update()
    for wall in wallList:
        wall.update()
    pg.display.update()

# main loop end --------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()