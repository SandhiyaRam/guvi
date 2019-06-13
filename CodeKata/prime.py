san=int(input())
if san>1:
  for i in range(2,san):
    if san%i==0:
      print('no')
      break
  else:
    print("yes")
else:
  print("no")        
