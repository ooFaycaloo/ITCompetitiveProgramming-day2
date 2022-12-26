t=[]
word=input("")
for i in word:
    t.append(i)
print(t)
y=len(t)
for i in range (y//2):
    x=t[i]
    t[i]=t[y-1]
    t[y-1]=x
    y=y-1
print (t)

