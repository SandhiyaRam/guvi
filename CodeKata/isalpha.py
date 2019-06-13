ss=input()
if any(a.isalpha() for a in ss):
  print("No")
elif any(a.isdigit() for a in ss):
  print('yes')  
