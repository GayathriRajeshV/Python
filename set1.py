#
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a^b)
#
seta={"Maya","Mamta","Mitra"}
seta.remove("Mitra")
print(seta)
#
set1={"Apple", "Banana"}
set2={"Banana", "Apple"}
setr=set1.copy()
print(setr)
#
e={1,2,3,4,5}
f={1,2,3,4,5}
g={1,2,3,4,5}
if(e==f==g):
    print( "Hence set have common elements")
else:
    print("Set do not have common elements")
#
def initials(full_name):
    initial=""
    if (len(full_name) == 0):
        return
    first_middle_last = full_name.split(" ")
    for name in first_middle_last:
        initial=initial+name[0].upper()+"."
    return initial
                
full_name="Gayathri Rajesh Valiyaparambil"
print(f"Initals generated: {initials(full_name)}")
#
import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

p=input("Enter a password:")
if (len(p)==8):
    break
elif(p=="[a-z]"):
    print("Password is valid")
else:
    print("Password is invalid")




