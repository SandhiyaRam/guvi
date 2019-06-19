
A,B,C=map(int,input().split())
ans=0
for i in range(1,C+1):
    ans+=A+(i-1)*B
print(ans)
