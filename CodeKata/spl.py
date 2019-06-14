sandy=input()
cc=0
for coc in sandy:
  if coc.isalpha()!=True and coc.isdigit()!=True and coc!=" ":
    cc=cc+1
print(cc)    
