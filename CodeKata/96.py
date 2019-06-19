
ai=list(input())
si=[]
for a in ai:
  if a not in si:
    si.append(a)
if ai==si:
  print('Yes')
else:
  print('No')
