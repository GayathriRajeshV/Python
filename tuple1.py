'''t = [(1, 2), (5, 6), (1, 3), (4, 8)]
f= [2, 5, 3]
a = []
for i in t:
    for j in i:
        if j in f:
            a.append(i)
print(a)


list = [(1, 2), (5, 6), (1, 3), (4, 8)]

x = [abs(b - a) for a, b in list]
a = max(x)
print(a)


t1=(1,2,3)
t2=(4,5,6)
m=t1+t2
print(m)'''


a=[[1,3,4],
   [3,6,8],
   [3,6,4]];
z=len(a)
for i in range(0,z):
    r=0
    for j in range (0,z):
        r=r+a[i][j]
    print("Sum of row",(i+1),":",r)
