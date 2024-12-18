#18/11/2024
#python
'''Ordered:When we say that tuples are ordered, it means that the items have a defined order,
and that order will not change.
Unchangeable:Tuples are unchangeable, meaning that we cannot change, add or remove itms after the tuples has been created.
Allow Duplicates:Since tuples are indexed, they can have items with the same value.'''

'''tuple1=("apple","banana","cherry","apple","cherry")
print(tuple1)

#find the length of the tuple
print(len(tuple1))

#tuple is also recognized by its index no.
print(tuple1[0])
print(tuple1[2])
print(tuple1[2:4])

#Tuple is a collection of element which can be of any type
tuple_A=("Gauri",45,"grade O",58000,"Mumbai")
print(tuple_A)
print(type(tuple_A))

#slicing a tuple
print(tuple_A[1:4])
print(tuple_A[2:])
print(tuple_A[:5])

#negative indexing
print(tuple_A[-2])
print(tuple_A[-1])

#Note:
#List is a collection which is ordered and changeable.
#List allows duplicate members.
#Tuple is a collection which is ordered and unchangeable.
#Tuple allows duplicate members

tuple_A=("Gauri",45,"grade O",58000,"Mumbai")
t2=list(tuple_A)
print(t2)

t2[2]="A in sports"
print(t2)

for i in t2:
    print(i)'''

#program to reverse the give tuple
tuple_2=(56,45,69,78,12)
print("The original tuple is:",tuple_2)
res=(tuple_2[::-1])
print("The reverse order is:")
print(res)

#to print even numbers in tuple
for i in tuple_2:
    if i%2==0:
        print(i)

tuple_3=(45,[23,89],80,63,25,45,45,90)
print(tuple_3[0])
print(tuple_3[1])
print(tuple_3[1][0])
print(tuple_3[1][1])

tuple_3[1][0]=45
print(tuple_3)

#program to count the 45 in the tuple
print("45 occurs",tuple_3.count(45),"times")
'''tuple cannot be changed'''
#tuple_3[2]=78
#print(tuple_3)

#program to create tuple with different data types
my_tuple=("Maggie",3,15.5,True)
print("I want to eat Maggie",my_tuple)

marks=(23,67,87,34)
print("i have got marks as:")
print(marks)

#program to create tuple with single item
price=(34,54)
print(price)







