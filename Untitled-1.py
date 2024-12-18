def isPalindrome(s):
    return s == s[::-1]
s = input("Enter a string:")
ans = isPalindrome(s)
if ans:
    print("Yes,string is a palindrome")
else:
    print("Nooo")

def number(num):
    num=int(input("Enter a number:"))
    temp=num
    rev=0
    while(num>0):
        digit=num%10
    rev=rev*10+digit
    num=num//10
    if(temp==rev):
        print("Yes")
    else:
        print("No")
