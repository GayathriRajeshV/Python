def max(n,m):
    if n>m:
        return n
    else:
        return m   

n=int(input("Enter first number:"))
m=int(input("Enter second number:"))

x=max(n,m)

print("Maximum of",n,"and",m,"is",x)

