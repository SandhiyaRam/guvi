sanda=input()
a=0
for i in sanda:
  if i=='0' or i=='1':
    a=a+1
  else:
    break
if a==len(sanda):
  print('yes')
else:
  print('no')
