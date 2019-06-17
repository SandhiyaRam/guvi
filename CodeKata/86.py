
uni=int(input())
if uni>0:
  for xui in range(2,uni):
    if(uni%xui==0):
      print("yes")
      break
  else:
      print("no")
else:
  print("no")
