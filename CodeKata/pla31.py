num=input()
open=[]
close=[]
for i in num:
    if i==")":
        open.append(i)
    else:
        close.append(i)
if len(open)==len(close):
    print("yes")
else:
    print("no")
    
