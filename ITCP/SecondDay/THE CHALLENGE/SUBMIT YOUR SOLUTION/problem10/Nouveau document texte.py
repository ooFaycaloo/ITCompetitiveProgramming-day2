t=[]
montone=1

t=[int(i) for i in input("donner t").split()]

if (t[1]<t[2]):
    for i in range(len(t)-1):
        if t[i]>t[i+1]:
            montone=0
elif (t[1]>=t[2]):
    for i in range(len(t)-1):
        if t[i]<t[i+1]:
             montone=1
print(montone)