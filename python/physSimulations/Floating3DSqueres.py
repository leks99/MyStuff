import time
import numpy
import pygame as py
from math import *
# settings -------------------------------------------------------------------------------------------------------------
settings_fps = 60 # default 60
settings_winXY = (1900, 1000) # default 1900 by 1000
settings_fullscreen = True #fullscreen
# end settings ---------------------------------------------------------------------------------------------------------

# set up stuff
clock = py.time.Clock()
resolution = (1920, 1080)
pScale = 1

# define variables
fps = settings_fps
winXY = settings_winXY
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
cubeOffsetX = winXY[0] // 2
cubeOffsetY = winXY[1] // 2
cubeXYZ = (winXY[0] // 2, winXY[1] // 2, 1)
cubeScale = 1
angleX = angleY = angleZ = 0
moveSpeed = 50

# events
run = True
addCube = True
rotateLeft = True
rotateRight = False
rotateUp = True
rotateDown = False
rotateClockwise = True
rotateClockwiseCounter = False
moveUp = True
moveDown = False
moveLeft = True
moveRight = False
moveForward = False
moveBackward = False

# define stuff
cubeList = []
projectionMatrix = [[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]

# define display (modify size in settings)
if settings_fullscreen == True:
    winXY = (0, 0)
    display = py.display.set_mode(winXY, py.FULLSCREEN)
else:
    display = py.display.set_mode(winXY)

# define objects (point lists)
cubePoints = [i for i in range(8)] # cube
cubePoints[0] = [[ 100], [ 100], [ 100], [1]]
cubePoints[1] = [[-100], [ 100], [ 100], [1]]
cubePoints[2] = [[ 100], [-100], [ 100], [1]]
cubePoints[3] = [[ 100], [ 100], [-100], [1]]
cubePoints[4] = [[-100], [-100], [ 100], [1]]
cubePoints[5] = [[ 100], [-100], [-100], [1]]
cubePoints[6] = [[-100], [ 100], [-100], [1]]
cubePoints[7] = [[-100], [-100], [-100], [1]]

# functions ------------------------------------------------------------------------------------------------------------
def multiplyMatrix(matrixA, matrixB):
    outputMatrix = numpy.dot(matrixA, matrixB)
    return outputMatrix

def drawPoint(point, coords):
    point[0] += coords[0]
    point[1] += coords[1]
    point[2] += coords[2]
    point2d = multiplyMatrix(projectionMatrix, point)
    perspectiveMatrix = [[1 / coords[2], 0, 0, 0],
                         [0, 1 / coords[2], 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]

    point2d = multiplyMatrix(perspectiveMatrix, point2d)

    x = point2d[0][0]
    y = point2d[1][0]
    py.draw.circle(display, GREEN, (x, y), 5)
    return x, y

def rotatePoint(point, angleX, angleY, angleZ):
    rotationMatrixX = [[1, 0, 0, 0],
                       [0, cos(angleX), -sin(angleX), 0],
                       [0, sin(angleX), cos(angleX), 0],
                       [0, 0, 0, 1]]
    rotationMatrixY = [[cos(angleY), sin(angleY), 0, 0],
                       [0, 1, 0, 0],
                       [-sin(angleY), cos(angleY), 1, 0],
                       [0, 0, 0, 1]]
    rotationMatrixZ = [[cos(angleZ), -sin(angleZ), 0, 0],
                       [sin(angleZ), cos(angleZ), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]
    point = multiplyMatrix(rotationMatrixX, point)
    point = multiplyMatrix(rotationMatrixY, point)
    point = multiplyMatrix(rotationMatrixZ, point)
    return point
def connectPoints(i, j, points):
    py.draw.line(display, WHITE, (points[i][0], points[i][1]), (points[j][0], points[j][1]))
def isCollidingFromRight(cube, cube2):
    if cube.mostToRightX >= cube2.mostToLeftX and cube.mostToLeftX <= cube2.mostToLeftX:
        if cube.mostToUpY <= cube2.mostToDownY and cube.mostToDownY >= cube2.mostToUpY:
            return True
    else:
        return False
def isCollidingFromLeft(cube, cube2):
    if cube.mostToLeftX <= cube2.mostToRightX and cube.mostToRightX >= cube2.mostToRightX:
        if cube.mostToUpY <= cube2.mostToDownY and cube.mostToDownY >= cube2.mostToUpY:
            return True
    else:
        return False
def isCollidingFromUp(cube, cube2):
    if cube.mostToUpY <= cube2.mostToDownY and cube.mostToDownY >= cube2.mostToDownY:
        if cube.mostToLeftX <= cube2.mostToRightX and cube.mostToRightX >= cube2.mostToLeftX:
            return True
    else:
        return False
def isCollidingFromDown(cube, cube2):
    if cube.mostToDownY >= cube2.mostToUpY and cube.mostToUpY <= cube2.mostToUpY:
        if cube.mostToLeftX <= cube2.mostToRightX and cube.mostToRightX >= cube2.mostToLeftX:
            return True
    else:
        return False
# end of functions -----------------------------------------------------------------------------------------------------

# class ----------------------------------------------------------------------------------------------------------------
class Camera:
    def __init__(self):
        self.f = 1
        self.s = 0
        self.xyz = (winXY[0] // 2, winXY[1] // 2, 200)
class Cube:
    def __init__(self, locationXYZ, rotationXYZ, scale, rotSpeedXYZ):
        self.mostToLeftX = 0
        self.mostToRightX = 0
        self.mostToUpY = 0
        self.mostToDownY = 0
        self.moveUp = False
        self.moveDown = True
        self.moveLeft = True
        self.moveRight = False
        self.moveForward = False
        self.moveBackward = False
        self.speedRotXYZ = rotSpeedXYZ
        self.scale = scale
        self.rotX = rotationXYZ[0]
        self.rotY = rotationXYZ[1]
        self.rotZ = rotationXYZ[2]
        self.rotXYZ = rotationXYZ
        self.x = locationXYZ[0]
        self.y = locationXYZ[1]
        self.z = locationXYZ[2]
        self.xyz = locationXYZ
        self.cubePoints = [i for i in range(8)]  # cube
        self.points = [0 for _ in range(len(self.cubePoints))]
    def update(self):
        if self.mostToLeftX <= 0:
            self.moveLeft = False
            self.moveRight = True
        if self.mostToUpY <= 0:
            self.moveDown = True
            self.moveUp = False
        if self.mostToRightX >= resolution[0]:
            self.moveLeft = True
            self.moveRight = False
        if self.mostToDownY >= resolution[1]:
            self.moveUp = True
            self.moveDown = False
        # move
        lastPos = self.xyz
        if self.moveUp:
            self.y += (moveSpeed * 2) * dt
        if self.moveDown:
            self.y -= (moveSpeed * 2) * dt
        if self.moveLeft:
            self.x += (moveSpeed * 2) * dt
        if self.moveRight:
            self.x -= (moveSpeed * 2) * dt
        if self.moveForward:
            self.z -= (moveSpeed / 10) * dt
        if self.moveBackward:
            self.z += (moveSpeed / 10) * dt
        self.xyz = (self.x, self.y, self.z)
        for cube in cubeList:
            if len(cubeList) > 1:
                if self != cube:
                    if isCollidingFromRight(self, cube):
                        self.moveLeft = True
                        self.moveRight = False
                    if isCollidingFromLeft(self, cube):
                        self.moveLeft = False
                        self.moveRight = True
                    if isCollidingFromUp(self, cube):
                        self.moveDown = True
                        self.moveUp = False
                    if isCollidingFromDown(self, cube):
                        self.moveDown = False
                        self.moveUp = True
        # set points
        self.cubePoints[0] = [[100], [100], [100], [1]]
        self.cubePoints[1] = [[-100], [100], [100], [1]]
        self.cubePoints[2] = [[100], [-100], [100], [1]]
        self.cubePoints[3] = [[100], [100], [-100], [1]]
        self.cubePoints[4] = [[-100], [-100], [100], [1]]
        self.cubePoints[5] = [[100], [-100], [-100], [1]]
        self.cubePoints[6] = [[-100], [100], [-100], [1]]
        self.cubePoints[7] = [[-100], [-100], [-100], [1]]
        # track points
        points = [0 for _ in range(len(self.cubePoints))]
        i = 0
        # rotate
        rotationMatrixX = [[1, 0, 0, 0],
                           [0, cos(self.rotX), -sin(self.rotX), 0],
                           [0, sin(self.rotX), cos(self.rotX), 0],
                           [0, 0, 0, 1]]
        rotationMatrixY = [[cos(self.rotY), 0, sin(self.rotY), 0],
                           [0, 1, 0, 0],
                           [-sin(self.rotY), 0, cos(self.rotY), 0],
                           [0, 0, 0, 1]]
        rotationMatrixZ = [[cos(self.rotZ), -sin(self.rotZ), 0, 0],
                           [sin(self.rotZ), cos(self.rotZ), 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]]

        self.mostToLeftX = 9999
        self.mostToRightX = 0
        self.mostToUpY = 9999
        self.mostToDownY = 0

        for point in self.cubePoints:

            '''cameraMatrix = [[(cam1.f * resolution[0]) / (2 * (resolution[0] * pScale)), cam1.s, 0, 0],
                            [0, (cam1.f * resolution[1]) / (2 * (resolution[1] * pScale)), 0, 0],
                            [0, -1, 1, 0],
                            [0, 0, 0, 1]]

            pointR = multiplyMatrix(cameraMatrix, point)'''

            pointR = multiplyMatrix(rotationMatrixX, point)
            pointR = multiplyMatrix(rotationMatrixY, pointR)
            pointR = multiplyMatrix(rotationMatrixZ, pointR)

            cameraMatrix = [[(cam1.f * resolution[0]) / (2 * (resolution[0] * pScale)), cam1.s, 0, 0],
                            [0, (cam1.f * resolution[1]) / (2 * (resolution[1] * pScale)), 0, 0],
                            [0, -1, 1, 0],
                            [0, 0, 0, 1]]

            pointR = multiplyMatrix(cameraMatrix, pointR)

            """perspectiveMatrix = [[1/pointR[2], 0, 0, 0],
                                 [0, 1/pointR[2], 0, 0],
                                 [0, 0, 1, 0],
                                 [0, 0, 0, 1]]

            pointR = multiplyMatrix(perspectiveMatrix, pointR)"""

            x, y = drawPoint(pointR, (self.xyz))
            """if x <= 0:
                self.moveLeft = False
                self.moveRight = True
            if y <= 0:
                self.moveDown = True
                self.moveUp = False
            if x >= resolution[0]:
                self.moveLeft = True
                self.moveRight = False
            if y >= resolution[1]:
                self.moveUp = True
                self.moveDown = False"""

            points[i] = (x, y)
            if x > self.mostToRightX:
                self.mostToRightX = x
            if x < self.mostToLeftX:
                self.mostToLeftX = x
            if y > self.mostToDownY:
                self.mostToDownY = y
            if y < self.mostToUpY:
                self.mostToUpY = y
            i += 1
        self.points = points

        connectPoints(0, 1, points)
        connectPoints(0, 2, points)
        connectPoints(0, 3, points)
        connectPoints(1, 4, points)
        connectPoints(1, 6, points)
        connectPoints(2, 4, points)
        connectPoints(2, 5, points)
        connectPoints(3, 5, points)
        connectPoints(3, 6, points)
        connectPoints(4, 7, points)
        connectPoints(6, 7, points)
        connectPoints(7, 5, points)


# class end ------------------------------------------------------------------------------------------------------------

lastTime = time.time()

# start of main loop ---------------------------------------------------------------------------------------------------
while run:

    # fps limiter (modify in settings)
    clock.tick(fps)
    dt = lastTime - time.time()
    lastTime = time.time()

    display.fill(BLACK)

    if addCube:
        cam1 = Camera()
        cubeList.append(Cube(cubeXYZ, (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        cubeList.append(Cube((0, 0, 1), (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        cubeList.append(Cube((0, 200, 1), (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        cubeList.append(Cube((0, 400, 1), (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        cubeList.append(Cube((300, 400, 1), (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        cubeList.append(Cube((600, 400, 1), (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        cubeList.append(Cube((1000, 400, 1), (angleX, angleY, angleZ), 1, (0.3, 0.3, 0.3)))
        addCube = False

    # rotate cubes
    for cube in cubeList:
        if rotateUp:
            cube.rotX += 1 * dt
        if rotateDown:
            cube.rotX -= 1 * dt
        if rotateLeft:
            cube.rotY -= 1 * dt
        if rotateRight:
            cube.rotY += 1 * dt
        if rotateClockwiseCounter:
            cube.rotZ += 1 * dt
        if rotateClockwise:
            cube.rotZ -= 1 * dt

    # look for events
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_DELETE:
                run = False
            if event.key == py.K_w:
                rotateUp = True
            if event.key == py.K_s:
                rotateDown = True
            if event.key == py.K_d:
                rotateRight = True
            if event.key == py.K_a:
                rotateLeft = True
            if event.key == py.K_e:
                rotateClockwise = True
            if event.key == py.K_q:
                rotateClockwiseCounter = True
            if event.key == py.K_DOWN:
                moveDown = True
            if event.key == py.K_UP:
                moveUp = True
            if event.key == py.K_LEFT:
                moveLeft = True
            if event.key == py.K_RIGHT:
                moveRight = True
            if event.key == py.K_r:
                moveForward = True
            if event.key == py.K_f:
                moveBackward = True
        if event.type == py.KEYUP:
            if event.key == py.K_w:
                rotateUp = False
            if event.key == py.K_s:
                rotateDown = False
            if event.key == py.K_d:
                rotateRight = False
            if event.key == py.K_a:
                rotateLeft = False
            if event.key == py.K_e:
                rotateClockwise = False
            if event.key == py.K_q:
                rotateClockwiseCounter = False
            if event.key == py.K_DOWN:
                moveDown = False
            if event.key == py.K_UP:
                moveUp = False
            if event.key == py.K_LEFT:
                moveLeft = False
            if event.key == py.K_RIGHT:
                moveRight = False
            if event.key == py.K_r:
                moveForward = False
            if event.key == py.K_f:
                moveBackward = False
    # update cubes
    for cube in cubeList:
        cube.update()

    py.display.update()

# end of main loop -----------------------------------------------------------------------------------------------------

py.quit()

if __name__ == '__main__':
    main()
