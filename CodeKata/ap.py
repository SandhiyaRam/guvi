nz,az,dz=map(int,input().split())
sz=0
for iz in range(1,nz+1):
  sz=sz+(az+(iz-1)*dz)
print(sz)
