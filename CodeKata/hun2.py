cou=int(input())
lissy=list(map(str,input().split()))
em=[]
m=lissy[0]
if lissy.count(m)==cou:
    print(m)
else:
    for i in range(len(lissy)):
        em.append(max(lissy))
        lissy.remove(max(lissy))
for i in em:
    print(i,end="")
