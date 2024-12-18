list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print(list)

list1=[1,2,2,2,2,3,5,4]
x=2
a=[i for i in list1 if i==x]
print(len(a))

list2=[1,2,3,4,5]
l=[]
for i in list2:
    l.insert(0,i)
print(l)

original_list = [1,2,3,4,5,6,7,8,9]
start = len(original_list) - 1
reversed_list = [original_list[i] for i in range(start, -1, -1)]
print(reversed_list)
