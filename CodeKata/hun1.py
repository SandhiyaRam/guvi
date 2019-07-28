num=input()
li=list(map(str,input().split()))
emp=[]
for i in li:
    co=li.count(i)
    if co>1:
        if i not in emp:
            emp.append(i)

emp.sort()
for i in emp:
    print(i,end=" ")
