#22/11/2024
#Function
#Function is self contained block of statement which has specific task to perform some of block of code can be reused whenever required

def myfunction():
    print("Hello ")

def remove duplicate(l):
    print(list(set(1)))

l=[78,85,69,12,90]
remove_duplicates(l)

#when to use Return

def rem_dup(12):
    return list(set(12))

l2=[78,58,45,67,67]

ans=rem_dup(12)
print("The clean daata is",ans)

#Write a program to calculate the factorial of a number
#using recursive

def factorial(n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

n=int(input("Enter a number"))
ans=factorial(n) #calling function
print("Factorial of",n,"is",ans)

#Dry run
'''
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1*factorial(0)
5*4*3*2*1*1
'''
