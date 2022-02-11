from math import sqrt

owce = 1000000
wt = sqrt(owce)
if wt % 1==0:
    lk = wt+wt
    print(int(lk))
else:
    uk = (int(wt)+1)
    ow = owce//wt + 1
    print(int(uk + ow))