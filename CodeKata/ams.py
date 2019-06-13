n15 = int(input())
sums = 0
tem = n15
while tem > 0:
   digit = tem % 10
   sums += digit ** 3
   tem //= 10
if n15 == sums:
   print("yes")
else:
   print("no")
