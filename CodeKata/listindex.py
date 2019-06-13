li=int(input())
lo=list(map(int,input().split()))
if li==len(lo):
  for i in range(li):
    print(lo[i],i)
