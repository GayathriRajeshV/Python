import random
PICK=random.randint(1,3)
CITY=["DELHI","MUMBAI","CHENNAI","KOLKATA"]
for I in CITY:
    for J in range (0,PICK):
        print(I,end="")
    print()
