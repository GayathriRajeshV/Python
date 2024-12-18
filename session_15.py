'''To present list in concise and easy way we use list comprehension.
As size of the code is less, performance will be increased'''

marks=[20,35,50,78,40]
new_marks=[] #empty list
for x in marks:
    new_marks.append(x+2)
print(new_marks)

#code using list comprehension

marks=[20,35,50,78,40]
new_marks=[x+2 for x in marks]
print(new_marks)

#list to set comprehension


#find cube of even number

cubes=[]
for x in range(11):
    if x%2==0:
        cubes.append(x**3)
print("listing for loops",cubes)

#using list comprehension
easy=[x**3 for x in range(11) if x%2==0]
print("Using list comprehension", easy)
