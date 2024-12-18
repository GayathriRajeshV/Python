#Dictionary
'''A dictionary is a built in data structure in Python that alows you to store a collection of key-value pairs.
Dictionary is mutable and it is unordered'''

my_dict={"std_id":123,"std_name":"Maya","Course":"MCA"}
print(my_dict)
print("\n")

x=my_dict["Course"]
print("The course selected is",x)
print("\n")

x=my_dict.get("std_id")
print(x)
print("\n")

#find all the keys present in the dictionary

y=my_dict.keys()
print("The keys present are:",y)
print("\n")

#To update particular value
my_dict.update({"std_name":"Sameer"})
print(my_dict)
print("\n")

#Adding items in the dictionary
my_dict["fees"]=70000
print(my_dict)
print("\n")

my_dict["std_add"]="Navi Mumbai"
print(my_dict)
print("\n")

#To remove certain values from the dictionary
my_dict.popitem()
print(my_dict)
print("\n")

#looping over dictionary
for i in my_dict:
    print (i)
print("\n")

#To GET keys from the list
for i in my_dict.values():
    print(i)
print("\n")

#To get values from the list
for i in my_dict.values():
    print(i)
print("\n")

for x,y in my_dict.items():
    print(x,y)
print("\n")




