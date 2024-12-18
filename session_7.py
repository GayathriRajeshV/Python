'''marks=[78,54,69,12,23]
print(min(marks))

print("The maximum value is",max(marks))

for i in range(0,5):
    for j in range(i+1,5):
        if marks[j]>marks[i]:
            temp=marks[i]
            marks[i]=marks[j]
            marks[j]=temp
print(marks)
print(marks[1])


#while loop is used to separate particular block of sentence again and again
#it is advisable to use while loop if we don't know the stopping criteria

#Program tp print hello 10 times
i=1 #initialization
while(i<=10):
    print("Hello")
    i+=1 #i=i+1


#table
#agar user se value lena hai tho 'n=int(input("Enter a number:"))'
#define karna hai tho 'n=10'
n=int(input("Enter a number:"))
i=1
while(i<=10):
    ans=n*i
    print(ans)
    i=i+1


#program to reverse a number n=123 rev=321
n=int(input("Enter a number "))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem #container
    n=n//10
print("This is reverse of a given number ",rev)'''


#program to check whether number is palindrom or not
n = int(input("Enter a number:"))
rev = 0
temp=n
while(num>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse of the given number is",rev)
if rev==temp:
    print("given number is palindrome")
else:
    print("given number is not palindrome")
