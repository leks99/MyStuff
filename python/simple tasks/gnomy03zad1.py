wiek = 0
print("podsj wiek")
wiek = int(input())
if wiek >= 18:
    print("możesz już oglądać filmy dla dorosłych")
if wiek == 17:
    print("aby obejrzeć ten film musisz zaczekać ", str(18 - wiek), "rok" )
else:
    print("aby obejrzeć ten film musisz zaczekać ", str(18 - wiek), "lat" )