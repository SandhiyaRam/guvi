nu=int(input())
lis=list(map(int,input().split()))
ciu=0
em=[]
for i in range(0,len(lis)):
    if lis.index(lis[i])==lis[i]:
        em.append(lis[i])
    if lis.count(lis[i])!=1:
        lis[i]="*"
       
for i in em:
    print(i,end=" ")
for i in lis:
    if lis.index(i)!=i:
        ciu=ciu+1
if ciu==nu:
    print("-1")
