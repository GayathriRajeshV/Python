'''#To repeat a particular block of statement

'''
'''syntax:
    for i inn range(start,end,step):
        block of code''''''

#program to print your namr 10 times
for i in range(1,11):
    print("Gayathri")

#program to print even numbers in list
l=[45,58,96,13,47,59,66,65,11]#creation of list
for i in l:
    if i%2==0:
        print(i)

#program to print table of a number
n=int(input("Enter a number "))
for i in range(1,11):
    ans=n*i
    print(ans)

#program to generate squares of number
for i in range(10,21):
    ans=i*i
    print(ans)

for i in range(10,21):
    ans=i**2 #exponntiation operator.
    print(ans)

#program to generate even numbers between 1 and 20
for i in range(1,21):
    if i%2==0:
        print(i)


start=int(input("Enter the start value: "))
end=int(input("Enter the end value: "))
for i in range(start,end+1):
    if i %2==0:
        print(i)

#print sum of first 10 natural numbers
sum1=0
for i in range(1,11):
    sum1=sum1+i
    print(sum1)
print("The range of first 10 natural numbers is",sum1)

#program to print factorial of numbers
#5!=5*4*3*2*1--->120
n=int(input("Enter a number "))
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print("Factorial of",n,"is",fact)'''

#use of break statement
for i in range(1,25):
    if(i==15):
        break
    print("hello",i)
print("lopp Excited")

#use of continue statement
for i in range(1,25):
    if(i==15):
        continue
    print("skipped 15")
print("lopp Excited") 































