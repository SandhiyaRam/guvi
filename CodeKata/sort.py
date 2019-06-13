f=int(input())
lisy=list(map(int,input().split()))
if f==len(lisy):
  lisy.sort()
for i in range(f):
  print(lisy[i],end=" ")
