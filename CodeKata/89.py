import math
sa,su=map(int,input().split())
ans=sa*su
root=math.sqrt(ans)
if int(root+0.5)**2==ans:
  print("yes")
else:
  print("no")  
