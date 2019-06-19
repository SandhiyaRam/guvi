nu=int(input())
li=list(map(int,input().split()))
sum=0
if len(li)==nu:
  for i in range(0,len(li)):
    sum=sum+int(li[i])
print(sum)    
