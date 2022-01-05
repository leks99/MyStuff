import random

year = 0
yearCounter = 0
startPopulation = 100
fertilityx = 18
fertilityy = 45

people = []

class Human:
    def __init__(self, age):
        self.gender = random.randint(0, 1)
        self.age = age

def reproduce(fertilityx, fertilityy):
    for human in people:
        if human.age >= fertilityx:
            if human.age <= fertilityy:
                if human.gender == 1:
                    if random.randint(1, 3) == 1:
                        people.append(Human(0))

def passyear():
    global year
    for human in people:
        human.age += 1
    year += 1

def showStats():
    print("amount of people:", str(len(people)), "after:", str(year), "years")

for i in range(startPopulation):
    people.append(Human(random.randint(1, 80)))

while len(people) < 100000 and len(people) > 1:
    reproduce(fertilityx, fertilityy)
    passyear()
    showStats()
