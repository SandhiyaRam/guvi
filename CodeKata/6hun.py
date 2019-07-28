num=int(input())
li=list(map(int,input().split()))
cu=0
for i in li:
    if li.count(i)>1:
        print(i)
        break
for i in li:
    if li.count(i)==1:
        cu=cu+1
if cu==num:
    print("unique")
