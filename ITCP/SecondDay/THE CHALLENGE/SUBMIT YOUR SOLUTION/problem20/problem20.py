prime=1
i=2
x=int(input("donnez x"))
if(x>1):
    while i<x-1:
        if (x%i==0):
            prime=0
        i=i+1
if prime==0 :
    print("not prime")
else:
    print("prime")


        
