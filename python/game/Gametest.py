import os
import time

promptLen = 30

def animRocket():
    distanceFromTop = promptLen - 4
    distanceFromLeft = 2
    os.system('cls')
    while True:
        for i in range(distanceFromTop):
            print("")
        if distanceFromTop > 3 and distanceFromLeft == 2:
            print("         /\         ")
            print("         ||         ")
            print("         ||         ")
            print("        /||\        ")
            distanceFromTop -= 1
        if distanceFromTop == 3 and distanceFromLeft < 50:
            print(" " * distanceFromLeft, "     ---\           ")
            print(" " * distanceFromLeft, "     -----------\   ")
            print(" " * distanceFromLeft, "     -----------/   ")
            print(" " * distanceFromLeft, "     ---/           ")
            distanceFromLeft += 2
        time.sleep(0.1)
        os.system('cls')




animRocket()