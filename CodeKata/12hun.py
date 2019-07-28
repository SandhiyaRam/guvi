num1,num2=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(0,num2-1):
    lis.remove(max(lis))
print(max(lis))    
    
