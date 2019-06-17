
rar=list(input())
if len(rar)%2==0:
    rar[int(len(rar)/2)] ='*'
    rar[int(len(rar)/2)-1]='*'
else:
    rar[int(len(rar)/2)] ='*'
for iui in range(0,len(rar)):
    print(rar[iui],end='')
