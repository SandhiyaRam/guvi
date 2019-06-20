
ni,zi=map(int,input().split())
li=list(map(int,input().split()))
lu=[]
if len(li)==ni:
	for i in range(0,len(li)):
		if li[i]%2!=0:
			lu.append(li[i])
print(lu[zi-1])
