print("wprowadz n: ")
n = int(input())
listaA = []
print("wprowadz numery pozostawionych obrazow: ")
for i in range(n):
    listaA.append(int(input()))
listaA.sort()
liczSkradzione = 0
for i in range(99999999):
    if i >= 1:
        if listaA[0+i]-1 != listaA[0+i-1]:
            liczSkradzione += 1
            listaA.append(listaA[0]+i)
            listaA.sort()
    if listaA[i] == listaA[-1]:
        break
print(liczSkradzione,listaA)