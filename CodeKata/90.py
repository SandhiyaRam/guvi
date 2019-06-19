numby=input()
li=list(numby)
#(li)
for i in range(0,len(li)):
  if int(li[i])%2!=0:
    print(li[i],end=' ')
