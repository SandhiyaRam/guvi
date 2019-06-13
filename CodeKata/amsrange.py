nos1,nos2 = map(int,input().split())
for i in range(nos1+1,nos2):
  sum = 0
  temp = i
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if i == sum:
    print(i,end=" ")
