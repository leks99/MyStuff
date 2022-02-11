# start - tratwa jedno miejsce
# co godzine - + jedno miejsce lub transport owiec
# pytanie - ile godz min. potrzeba na transport wszystkich owiec
# input - liczba n (2<= n <= 10do18) to liczba owiec
# output - liczba oznaczajaca licz godzin

# setup
tratwa = 0
owce = int(input())
odp = 0

# math
x = owce//2
owce -= x*2
odp += x+2
if owce>0:
    odp += 1
print(odp)

