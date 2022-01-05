print("ile krokow: ")
n = int(input())
print(": ")
listaRaw = input().split()
lista = [int(i) for i in listaRaw]
a = 0
schodki = []
for i in range(len(lista)):
    if lista[i] == 1:
        a += 1
        schodki.append(1)
    if i >= 1:
        if lista[i] > lista[i-1]:
            schodki[a-1] += 1
print(a)
print(schodki)