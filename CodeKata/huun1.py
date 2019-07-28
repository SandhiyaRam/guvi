num=input()
li=list(map(str,input().split()))
emp=[]
temp=0
for i in li:
    co=li.count(i)
    if co>1:
        if i not in emp:
            emp.append(i)
            emp.sort()
for i in emp:
    print(i,end=" ")
for i in li:
    if li.count(i)==1:
        temp=temp+1
if str(temp)==num:
    print("unique")
