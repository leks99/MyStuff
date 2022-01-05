import random

for i in range(10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print("---------------------------------------------")
    print("liczba", str(a), "pomnozona przez", str(b), "to: ")
    x = int(input())
    if x == a * b:
        print("gratulacje!")
    else:
        print("źle")