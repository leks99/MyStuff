import random

a = random.randint(1, 10)
b = random.randint(1, 10)

print("pierwsza losowa liczba to ", str(a), " a  druga to ", str(b))

print("podaj wartość iloczynu tych liczb: ")
x = float(input())

if x == a/b:
    print("gratulacje!")
else:
    print("źle")
