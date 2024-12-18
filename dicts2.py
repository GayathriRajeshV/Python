stu_marks={"Jaya Surya":80,"Rahul":83,"Mayuresh":80,"Somesh":76,"Kajal":79,"Gayathri":90}
# marks=sorted(stu_marks.values())
marks= sorted([(value, key) for (key, value) in stu_marks.items()])
# {sort bhi predefined hai upar wala statment ye bolta hai ki "value,key" aur "key,value" jo stu_marks mai jo haina vo sort karke predefine se sort hojayega}
# marks=str(marks)
print(marks)
for i in reversed(marks):
    # {ye reverse karne ke leye hota hai aisa reversed laga ke pre defined hai voh }
    print(i)

# print(marks)
# marks=int(marks)
# print(type(marks))
# print(len(marks))

# c=dict(reversed(dict(marks.items())))
# print(str(c))
# print(list(reversed(marks)))
# print(str(marks))

