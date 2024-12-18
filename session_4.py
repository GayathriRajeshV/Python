#07/11/24
#Program to accept score of two team and make a decision which team won the match
india=int(input("Enter score of India "))
pak=int(input("Enter score of Pakistan "))
if india > pak:
    print("Team India wins the match")
else:
    print("Team Pakistan wins the match")

#Program to find latest number among three
num1=int(input("Enter a 1st number "))
num2=int(input("Enter a 2st number "))
num3=int(input("Enter a 3st number "))

if num1>num2 and num1>num3 :
    print(num1,"is greatest")
    
elif num2>num3 and num2>num3:
    print(num2,"is greatest")
    
else:
    print(num3,"is greatest")

#loop
#Whenever we want to repeat particular block of statment again and again we use loop.
#Types
#1)for loop
#2)while loop

#Print 1 to 10
for i in range(20):
    print(i)
print("----------|----------")

for i in range(1,15):#in python last value is always excluded
    print(i)
print("----------|----------")

for i in range(1,15,3):
    print(i)
print("----------|----------")

#Program to print tables

num=int(input("Enter a number "))
for i in range(1,11):
    ans=num*i
    print(ans)

num=1
for i in range(1,3):
    for i in range(1,11):
        ans=num*i
        print(ans)

# Multiplication table for 1 and 2
for i in range(1, 11):  # Adjust the range if you want a different range
    print(1 x {i} = {1 * i})
    print(2 x {i} = {2 * i})


    
          







