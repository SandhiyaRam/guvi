ma,sa=map(int,input().split())
lica=list(map(int,input().split()))
cud=0
if ma==len(lica):
  for ai in range(ma):
    if lica[ai]==sa:
      cud=cud+1
  print(cud)      
