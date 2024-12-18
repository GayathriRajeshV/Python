try:
    x=int(input("Enter number upto 10000:"))
    if x >10000:
        raise ValueError(x)
except ValueError:
    print(x,"is out of range")
else:
    print(x,"is within the range")
