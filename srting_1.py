num=input("Enter a list of number:")
list=num.split()
sum=0
for i in list:
    sum=sum+int(i)
print("Total is",sum)
