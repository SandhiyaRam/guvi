
no1,no2=map(int,input().split())
def GCD(no1,no2):
    if(no2==0):
        return no1
    else:
        return GCD(no2,no1%no2)
ji=GCD(no1,no2)
print(ji)
