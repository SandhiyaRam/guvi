def factorial(ns):
  if (ns==1 or ns==0):
    return 1; 
  else: 
    return ns * factorial(ns - 1);  
  
nuum=int(input()) 
print(factorial(nuum)) 
  
