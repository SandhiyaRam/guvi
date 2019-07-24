
sw,dw=map(str,input().split())
c=0
co=0
for i in range(len(sw)):
    if sw[i]==dw[i]:
        co=co+1
    else:
         c=c+1
if c==1:
    print("yes")
else:
    print("no")
