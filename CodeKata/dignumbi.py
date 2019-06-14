sand=input()
coo=False
cus=False
for ii in sand:
  if ii.isalpha():
    coo=True
  if ii.isdigit():
    cus=True
if coo==True and cus==True:
  print("Yes")
else:
  print("No")        


    

    

