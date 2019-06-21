
def f(nu):
  if (nu==1 or nu==0):
    return 1; 
  else: 
    return nu * f(nu - 1);  
  
ni=int(input()) 
print(f(ni)) 
