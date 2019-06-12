n,m=map(int,input().split())
lis=list(map(int,input().split()))
sum=0
if n==len(lis):
  for i in range(len(lis)+1):
    if i<m:
      sum=sum+lis[i]
  print(sum)  
