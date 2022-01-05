kod = ""
listkod = []

while True:
    print("podaj kod: ")
    kod = str(input())
    if len(kod) > 100000:
        print("za długi kod! podaj jeszcze raz")
    else:
        break

while True:
    print("podaj ilość modyfikacji kodu: ")
    n = int(input())
    if n <= 1:
        print("za mało! podsaj jeszcze raz")
    elif n >= 1000000:
        print("za dużo! podaj jeszcze raz")
    else:
        break

for i in kod:
    listkod.append(i)

for i in range(n):
    print("-------------------")
    print("podaj c1:")
    c1 = str(input())
    print("podaj c2:")
    c2 = str(input())
    for i in range(len(listkod)):
        if listkod[i] == c1:
            listkod[i] = c2

kod = "".join(listkod)
print(kod)
