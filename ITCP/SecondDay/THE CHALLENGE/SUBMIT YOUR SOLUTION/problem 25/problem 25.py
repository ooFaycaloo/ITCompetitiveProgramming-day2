s1=1
s2=2
t=[1,1,2]
for i in range (100):
    s1=s1+s2
    t.append(s1)
    s2=s1+s2
    t.append(s2)

print(t)