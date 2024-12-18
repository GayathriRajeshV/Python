a=input("Enter the Password:")
c1,c2,c3=0,0,0
for i in a:
    if (i.islower()):
        c1=c1+1
    elif(i.isupper()):
        c2=c2+1
    elif(i.isnumeric()):
        c3=c3+1
if((c1>=1 and c2>=1) and (c3>=1 and len(a)==8)):
    print("Valid Password")
else:
    print("Try Again")
