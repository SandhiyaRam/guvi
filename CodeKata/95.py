
Sa=input()
l1=[]
l2=[]
for a in range(0,len(Sa)):
    if (a%2==0):
        l1.append(Sa[a])
    else:
        l2.append(Sa[a])
print("".join(l1),"".join(l2))
