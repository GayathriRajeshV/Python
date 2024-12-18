#30/10/2024
#Arithmetic operators +,-,*,/,%
a=int(input("Enter a 1st number "))
b=int(input("Enter a 2nd number "))
add=a+b
print("The answer for Addition:",add)
sub=a-b
print("The answer for Subtraction:",sub)
mul=a*b
print("The answer for Multiplication:",mul)
div=a/b
print("The answer for Division:",div)
mod=a%b
print("The answer for Modulus:",mod)


#Simple Interest
Principal = float(input("Enter the Principal amount: "))
Time = float(input("Enter the Time: "))
Rate = 5
print("Rate = 5")
SI = (Principal * Rate * Time) / 100
print("The Simple Interest is", SI)


#Average of three numbers
a=float(input("Enter a 1st number "))
b=float(input("Enter a 2nd number "))
c=float(input("Enter a 3rd number "))
avg = (a + b + c) / 3
print("Average of 3 numbers is ",avg)

#CONDITIONAL STATEMENTS
#if
#if...else
#if...elif...else
#print welcome message on receipt of positive integer value
input=int(input("Enter a number "))
if(input>0):
    print("Hello World")

#Print user input if number is positive then welcome else invalid user
pin = int(input("Enter a pin"))
if(pin>0):
    print("Welcome to Bank")
else:
    print("Invalid")

#Check greatest number among two
a=float(input("Enter a 1st number "))
b=float(input("Enter a 2nd number "))
if(a>b):
    print("a is greater")
else:
    print("b is greater")
    
#Eligible to vote
age=int(input("Enter a number "))   
if(age>=18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")
    







