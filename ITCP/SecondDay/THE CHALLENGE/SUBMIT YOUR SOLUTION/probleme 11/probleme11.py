word=input("your word")
def checkword(word):
    for l in word :
        if (l.islower()==1):
            return False
    print("true word")       
print(checkword(word))