import time

def przeszukaj_listę(list, target):
    l = 0
    r = len(list)
    current = 0
    licznik = 1

    while l < r:
        current = (l + r) // 2
        print("dzieli na pół: "+str(current))

        if list[current] == target:
            return current,licznik
        else:
            if list[current] < target:
                l = current+1
                print("szuka: "+ str(l) +"-"+ str(r))
            else:
                r = current
                print("szuka: " + str(l)+"-"+str(r))
        print(" ")
        licznik += 1

lista1 = []
for i in range(1001):
    lista1.append(i)

current, licznik = przeszukaj_listę(lista1, 364)
print("-----znalazł!-----")
print(current)
print("za "+str(licznik)+" razem")
