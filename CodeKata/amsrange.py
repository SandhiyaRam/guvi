nosum1,nosum2 = map(int,input().split())
for ii in range(nosum1+1,nosum2):
  sumu = 0
  tempu = ii
  while tempu > 0:
    digits = tempu % 10
    sumu += digits ** 3
    tempu //= 10
  if ii == sumu:
    print(ii,end=" ")
