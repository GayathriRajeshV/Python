list=[1,1,2,2,2,2,3,3,3,4,4,5,6,6]
k=1
a=[]
for i in list:
    frequency=list.count(i)
    if frequency > k and i not in a:
        a.append(i)
print(a)

list1=[1,2,3,4,5,6,7,8]
odd=[]
for num in list1:
    if num % 2 != 0:
        odd.append(num)
print(odd)
print("Sum of odd number is",sum(odd))

list3=[1,5,6,3]
list4=[4,8,6,1]
result=[i for i in list3 if i in list4]
print(result)

list6=[1,2,5,6,2,2,8]
list5=[]
for num in list6:
    if num not in list5:
        list.append(num)
print(list5)


