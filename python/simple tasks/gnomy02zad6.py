print("podaj pierwszą liczbę: ")
x = int(input())
print("podaj drugą liczbę: ")
y = int(input())

print("zgadnij sumę tych liczb: ")
wynik = int(input())

if wynik == x+y:
    print("gratulację! poprawna odpowiedź!")
else:
    print("idź się uczyć matmy!")