a=int(input("Enter The Value For a:"))
b=int(input("Enter The Value For b:"))
c=int(input("Enter The Value For c:"))
sum=a+b+c
print(sum,"is the Sum of three number")
avg=(a+b+c)/3
print(avg,"is the average of three numbers")
if(a>b and a>c):
    print(a,"is the largest")
elif(b>a and b>c):
    print(b,"is the largest")
else:
    print(c,"is the largest")
