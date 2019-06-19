
ny=int(input())
li=list(map(int,input().split()))
a=li[0]
if ny==len(li):
    for i in range(1,len(li)):
        if li[i]>a:
              a=li[i]
        else:
            print(i-1)
            break
