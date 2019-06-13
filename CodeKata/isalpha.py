ss=input()
if any(a.isalpha() for a in ss):
  print("no")
elif any(a.isdigit() for a in ss):
  print('yes')  
