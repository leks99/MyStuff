print("podaj pierwszą liczbę: ")
x = float(input())

print("podaj liczbę prpzez którą chcesz dzielić: ")
y = float(input())

if y == 0:
    print("nie dzieli się przez zero!!!")
else:
    print("wynik to: ", str(x / y))