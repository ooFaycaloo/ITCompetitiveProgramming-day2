label = "label"
print("itcFLAG{", end="")
for x in label:
    print(chr(ord(x)^13), end="")
print("}")
