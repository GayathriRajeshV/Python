#04/11/21
#Variable should be in small letters
#Even or odd
#If number is divisible by 2 i.e. remainder is 0 or not
num=int(input("Enter a Positive integer "))
if num%2==0:# == is comparison operator(<,>,<=,>=,==,!=)
    print(num,"is a even number")
else:
    print(num,"is a odd number")


#Program to check whether the entered number is divisible by 3 and 5
num=int(input("Enter a Positive integer "))
if num%3==0 and num%5==0:
    print(num,"is a divisible by both 3 and 5")
else:
    print(num,"is not divisible by both 3 and 5")

    
#Program to check whether the entered number is divisible by 3 or 7
num=int(input("Enter a Positive integer "))
if num%3==0 or num%7==0:
    print(num,"is a divisible by both 3 and 7")
else:
    print(num,"is not divisible by both 3 and 7")


#if-elif-else(to validate multiple condition)
#Check whether the number is zero, positive or negative
a=int(input("Enter a number "))
if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,"is a negative number")
else:
    print("It is 0")
    
#
a=int(input("Enter a number "))
if a>0:
    print(a,"is a positive number")
elif a<0:
    print(a,"is a negative number")
elif a==0:
    print("It is 0")   
else:
    print("Enter correct values")
    

#Program to accept percentage from user and make a decision about his grade.
marks=int(input("Enter a marks "))
if marks>70:
    print("Your grade is O")
    print("Congratulations")
elif marks>60:
    print("Your grade is A")
elif marks>40:
    print("Your grade is B")   
else:
    print("Failed")


#Program to generate electricity bill
unit=int(input("Electricity unit consumed "))
if unit>0 and unit<=100:
    bill=unit*10
    print("Your bill is",bill,"rs/unit")

elif unit>100 and unit<=200:
    bill=100*10+(unit-100)*15
    print("Your bill is",bill,"rs/unit")
    
elif unit>200 and unit<=300:
    bill=100*10+100*15+(unit-200)*20
    print("Your bill is",bill,"rs/unit")
    
else:
    bill=100*10+100*15+100*20+(unit-300)*25
    print("Your bill is",bill,"rs/unit")


































    
    
    


    


    
    
