a1=[]
a2=[]
a3=[]
a1=[int(i) for i in input("donner a1").split()]
a2=[int(i) for i in input("donner a2").split()]

for i in a1 :
    for j in a2:
        if i==j:
            a3.append(i)
        else:
            continue

print (a3)