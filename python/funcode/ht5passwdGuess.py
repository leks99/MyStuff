import time
import hashlib as hl
import numpy as np

passwdR = "zzzz"

passwd = hl.md5(passwdR.encode()).hexdigest()
passwdSymbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
passwdSymbolsT = np.array(passwdSymbols)
passwdLength = len(passwd)
PSL = len(passwdSymbols)

start = time.time()

for i in range(PSL ** passwdLength):
    passwdGuess = passwdSymbolsT.item((((i // PSL) // PSL) // PSL) % PSL)+passwdSymbolsT.item(((i // PSL) // PSL) % PSL)+passwdSymbolsT.item((i // PSL) % PSL)+passwdSymbolsT.item(i % PSL)
    """passwdGuess = passwdSymbols[(((i // PSL) // PSL) // PSL) % PSL]
    passwdGuess += passwdSymbols[((i // PSL) // PSL) % PSL]
    passwdGuess += passwdSymbols[(i // PSL) % PSL]
    passwdGuess += passwdSymbols[i % PSL]"""
    if hl.md5(passwdGuess.encode()).hexdigest() == passwd:
        print("haslo:", passwd, "odgadniete:", hl.md5(passwdGuess.encode()).hexdigest(), passwdGuess)
        break

end = time.time()
print("czas wykonania 1: ", end-start, "s")

start = time.time()

for i in passwdSymbols:
    for x in passwdSymbols:
        for y in passwdSymbols:
            for z in passwdSymbols:
                passwdGuess = i+x+y+z
                if hl.md5(passwdGuess.encode()).hexdigest() == passwd:
                    print("haslo:", passwd, "odgadniete:", hl.md5(passwdGuess.encode()).hexdigest(), passwdGuess)
                    break

end = time.time()
print("czas wykonania 2: ", end-start, "s")
