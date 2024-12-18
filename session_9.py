#16/11/2024
#program to get sum of digits present in a number
n = int(input("Enter a number:"))
s = 0
while(n>0):
    rem = n%10
    s=s+rem
    n=n//10
print("Sum of the number",+n,"is",rem)

#program to check whether the number is armstrong number or not
#example 153,371

num = int(input("Enter a number:"))
s = 0
temp=num
while(num>0):
    digit = temp%10
    s=digit**3
    temp=temp//10

if num == s:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

#Set
'''A set in python programming is an unordered collection data type that is iterable and has no duplicate elements.
while sets are mutable, meaning you can add or remove elememnt after their creation'''

set_A={5,3,8,1}
print(set_A,"\n")

#set does not allow duplicate values.
set_B={6,10,10,4}
print(set_B)

#set union operation
set_C=set_A.union(set_B)
print("\nThe union of both the sets are:",set_C)

set_D=set_A.union(set_B,set_C)
print("\nThe union of both the sets are:",set_D)

#using union operator |
result=set_A|set_B|set_C
print("\nThe union of all is",result)

#To find intersection of two sets using intersection() function and & operator
set_1={11,12,45,61}
set_2={74,12,61,21}
set_3=set_1.intersection(set_2)
print(set_3)

set_3=set_1 & set_2
print(set_3)

#set difference(-)
result=set_1-set_2
print("\nThe difference is",result)

#set difference using difference() method
result=set_1.difference(set_2)
print("\nThe difference of both the sets are:",result)

#To get symetric difference (elements which are not in both the sets)
result=set_1 ^set_2
print("\nThe symetric difference of the set is:",result)

result=set_1.symmetric_difference(set_2)
print("\nThe symetric difference of the set is:",result)











