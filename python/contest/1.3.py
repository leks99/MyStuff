# start - tratwa jedno miejsce
# co godzine - + jedno miejsce lub transport owiec
# pytanie - ile godz min. potrzeba na transport wszystkich owiec
# input - liczba n (2<= n <= 10do18) to liczba owiec
# output - liczba oznaczajaca licz godzin

# setup
from math import sqrt, ceil
owce = 1000000

# math
if owce > 1:
    if owce%2 == 1:
        owce += 1
    owceA = ceil(sqrt(owce))
    kursy = ceil(owce / owceA)
    odp = owceA+kursy
else:
    if owce == 1:
        odp = 2
    elif owce == 0:
        odp = 0

print(odp)

