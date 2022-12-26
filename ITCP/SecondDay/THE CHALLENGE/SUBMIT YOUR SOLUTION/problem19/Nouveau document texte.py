x=int(input())
i=1
sum=0
while i<x:
    if (x%i==0):
        sum=sum+i
        i=i+1
    else:
        i=i+1
    
if (x==sum):
    print("perfect number")
else:
    print("False")