nq,aq,dq=map(int,input().split())
sq=0
for iq in range(1,nq+1):
  sq=sq+(aq+(iq-1)*dq)
print(sq)
