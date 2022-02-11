from math import sqrt, ceil
from decimal import *
owce = int(input())

#------------------------------
if owce > 1:
    owceA = Decimal(owce)
    owceA = owceA.sqrt()
    #owceA = sqrt(owce)
    kursy = Decimal(owce) / owceA
    odp = ceil(owceA+kursy)
else:
    odp=2 if owce==1 else 0
print(odp)
#-------------------------------
