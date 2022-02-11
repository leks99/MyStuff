# start - tratwa jedno miejsce
# co godzine - + jedno miejsce lub transport owiec
# pytanie - ile godz min. potrzeba na transport wszystkich owiec
# input - liczba n (2<= n <= 10do18) to liczba owiec
# output - liczba oznaczajaca licz godzin

# metoda wszystkie kombinacje

# setup
tratwa = 0
owce = int(input())
odpowiedzi = []
owceTemp = 0

# math
while tratwa<=owce//2:
    czas = 0
    tratwa += 1
    czas += tratwa
    owceTemp = owce
    while owceTemp>0:
        owceTemp -= tratwa
        czas += 1
    odpowiedzi.append(czas)


print(min(odpowiedzi))

