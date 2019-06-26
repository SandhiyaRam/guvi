
nu=int(input())
i=list(input())

li=["a","e","i","o","u","A","E","I","O","U"]
for ii in i:
  if ii in li:
    i.remove(ii)
j=i[::-1]
for i in j:
  print(i,end="")    
