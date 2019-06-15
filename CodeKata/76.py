shan=int(input())
if shan>1:
  for ice in range(2,shan):
    if shan%ice==0:
      print('no')
      break
  else:
    print("yes")
else:
  print("no")      
