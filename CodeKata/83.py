numby=int(input())
sa1,sa2=map(int,input().split())
cuc=0
for i in range(sa1+1,sa2):
	if i==numby:
		cuc=cuc+1
if cuc>0:
	print('yes')
else:
	print('no')
