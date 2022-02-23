import pygame
import os
from Tank import *
from Bullet import *
from HUD import *
from BlankObject import *
from Maps import *

# ---------SETTINGS-----------
WINDOW_W, WINDOW_H = 1000, 600  # (default 1900 by 1000)
FPS = 60
DEBUG = False
# ----------------------------

# ---------constants----------
BACKGROUND_COLOR = (80, 80, 80)
WHITE = (255, 255, 255)
BLACK = (255, 255, 255)
tankImageScale = 0.08
tankImageDimensionX = 616 * tankImageScale
tankImageDimensionY = 692 * tankImageScale
tankImageDimensions = (int(tankImageDimensionX), int(tankImageDimensionY))
# ----------------------------

# ------import textures-------
icon = pygame.image.load("playerTank.png")
playerTankImagePre = pygame.image.load("playerTank.png")
playerTankImage = pygame.transform.scale(playerTankImagePre, tankImageDimensions)
enemyTankImagePre = pygame.image.load("enemyTank.png")
enemyTankImage = pygame.transform.scale(enemyTankImagePre, tankImageDimensions)
# ----------------------------

# -----------setup------------
display = pygame.display.set_mode((WINDOW_W, WINDOW_H))
run = True
clock = pygame.time.Clock()
pygame.display.set_caption("czolgi2:)")
pygame.display.set_icon(icon)
pygame.init()
allList = []
key_w_isPressed = False
key_s_isPressed = False
key_a_isPressed = False
key_d_isPressed = False
key_space_isPressed = False
key_up_isPressed = False
key_down_isPressed = False
key_left_isPressed = False
key_right_isPressed = False
key_rctrl_isPressed = False
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 40)
HUD = HUD(font)
# ----------------------------

# -----------init map---------
player, enemy = map1(allList, playerTankImage, tankImageDimensions, enemyTankImage)
# ----------------------------

# ----------------------------MAIN GAME LOOP---------------------------------
while run:
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
            # enemy
            if event.key == pygame.K_UP:
                key_up_isPressed = True
            if event.key == pygame.K_DOWN:
                key_down_isPressed = True
            if event.key == pygame.K_LEFT:
                key_left_isPressed = True
            if event.key == pygame.K_RIGHT:
                key_right_isPressed = True
            if event.key == pygame.K_RCTRL:
                key_rctrl_isPressed = True

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
            # enemy
            if event.key == pygame.K_UP:
                key_up_isPressed = False
            if event.key == pygame.K_DOWN:
                key_down_isPressed = False
            if event.key == pygame.K_LEFT:
                key_left_isPressed = False
            if event.key == pygame.K_RIGHT:
                key_right_isPressed = False
            if event.key == pygame.K_RCTRL:
                key_rctrl_isPressed = False

    #  player events ----------------------
    if key_w_isPressed:
        player.goUp(allList)
    elif key_s_isPressed:
        player.goDown(allList)
    elif key_a_isPressed:
        player.goLeft(allList)
    elif key_d_isPressed:
        player.goRight(allList)
    if key_space_isPressed:
        player.shoot(allList)
        key_space_isPressed = False

    #  enemy events -----------------------
    if key_up_isPressed:
        enemy.goUp(allList)
    elif key_down_isPressed:
        enemy.goDown(allList)
    elif key_left_isPressed:
        enemy.goLeft(allList)
    elif key_right_isPressed:
        enemy.goRight(allList)
    if key_rctrl_isPressed:
        enemy.shoot(allList)
        key_rctrl_isPressed = False

    for object in allList:
        object.update(allList)
        if object.destroy:
            if object.team == 99:
                allList.remove(object)
            else:
                allList[allList.index(object)] = BlankObject()

    if DEBUG:
        print("------------allList-------------")
        print(allList)
        print("objects: ", len(allList))

    display.fill(BACKGROUND_COLOR)
    for object in allList:
        object.draw(display, DEBUG)
    HUD.draw(allList, display)

    pygame.display.update()
# --------------------------END OF GAME LOOP-----------------------------------

pygame.quit()

"""
--------------------------------------------Manual-----------------------------------------
object.team / 0=player, 1=enemy, 100=blank, 99=bullet, 98=wall, 89=HPBooster, 
88=ammoBooster
object.direction (x, y) / (1, 0) = Right / (-1, 0) = Left
object.velocity -bullet only- direction*speed (x, y) / (9, 0)
-------------------------------------------------------------------------------------------
"""

