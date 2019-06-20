import math
gi,hi=input().split()
gi=int(gi)
hi=int(hi)
fi=(math.gcd(gi,hi))
print((gi*hi)//fi)
