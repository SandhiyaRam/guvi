sa=input()
s=list(sa)
ca=s[0]
s[0]=s[1]
s[1]=ca
t=s[2]
s[2]=s[3]
s[3]=t
for i in range(0,4):
    print(s[i],end="")
#print(s[0],s[1],s[2],s[3])

