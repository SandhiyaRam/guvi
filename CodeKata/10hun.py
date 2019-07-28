num1=int(input())
num2=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
for i in li2:
    if i in li1:
        print("YES")
        break
    else:
        print("NO")
        break
