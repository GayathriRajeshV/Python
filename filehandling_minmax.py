f=open("a.txt","r")
a=f.readlines()
res=[eval(i) for i in a]
small=res[0]
large=res[0]
for i in res:
    if i>large:
        large=i
    elif i<small:
        small=i
print("smallest no.",small,"and largest no.",large)
