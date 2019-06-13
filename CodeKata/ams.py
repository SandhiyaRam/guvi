n15 = int(input())
sums = 0
temp = n15
while temp > 0:
   digit = temp % 10
   sums += digit ** 3
   temp //= 10
if n15 == sums:
   print("yes")
else:
   print("no")
