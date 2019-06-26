
aa,bb=input().split(" ")
aa=int(aa)
bb=int(bb)
co=0
for i in range(aa,bb+1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
                
        else:
            co=co+1
print(co)
