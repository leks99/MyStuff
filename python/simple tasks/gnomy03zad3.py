

while True:
    print("--------------------------------")
    print("wybierz co chcesz zrobić: ")
    print("  1.dodawanie")
    print("  2.odejmowanie")
    print("  3.dzielenie")
    print("  4.mnożenie")
    print("  5.wyjdź")
    print("wybieram: ")
    wybor = int(input())

    if wybor == 1:
        print("-----------------------")
        print("pierwsza liczba: ")
        x = int(input())
        print("druga liczba: ")
        y = int(input())
        print("-----------------------")
        print("wynik dodawania to: ", str(x + y))
    if wybor == 2:
        print("-----------------------")
        print("pierwsza liczba: ")
        x = int(input())
        print("druga liczba: ")
        y = int(input())
        print("-----------------------")
        print("wynik odejmowania to: ", str(x - y))
    if wybor == 3:
        print("-----------------------")
        print("pierwsza liczba: ")
        x = int(input())
        print("druga liczba: ")
        y = int(input())
        if y == 0:
            print("nie dziel przez zero!!!")
        else:
            print("-----------------------")
            print("wynik dzielenia to: ", str(x / y))
    if wybor == 4:
        print("-----------------------")
        print("pierwsza liczba: ")
        x = int(input())
        print("druga liczba: ")
        y = int(input())
        print("wynik mnożenia to: ", str(x * y))
    if wybor == 5:
        break