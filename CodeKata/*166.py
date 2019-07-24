num=int(input())
li=list(map(int,input().split()))
for i in li:
    cou=li.count(i)
    #print(cou)
    if cou==1:
        print(i)
    #else:
     #   break

