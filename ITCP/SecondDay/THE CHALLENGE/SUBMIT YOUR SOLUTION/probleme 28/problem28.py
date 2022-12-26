a=int(input("donner a"))
b=int(input("donner b"))
n=int(input("donner n"))

for i in range (n):
    print('IT')
    if (i%a!=0)and(i%b!=0):
        print(i)
    elif (i%a==0)and(i%b!=0):
        print('IT')
    elif (i%b==0)and (i%a!=0):
        print('CCC')
    elif (i%b==0)and (i%a==0):
        print('ITCCC')
    