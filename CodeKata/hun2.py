count=int(input())
lissy=list(map(str,input().split()))
em=[]
for i in range(len(lissy)):
    em.append(max(lissy))
    lissy.remove(max(lissy))
for i in em:
    print(i,end="")
