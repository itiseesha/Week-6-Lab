name=input("Hey buddy, what's your last name? ")
print(name[0:1])
if (name=="Solomon"):
    print("Congradulations, you have the best name!")
elif (name[0:1]>='A' and name[0:1]<='M' or name[0:1]>='a' and name[0:1]<='m'):
    print("Congratulations, because of the alphabet, you will always be in front!")
else:
    print("rip, cause of the alphabet you will always be towards the end of the line")