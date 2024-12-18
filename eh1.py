'''try:
    num=int(input("Enter a integer number:"))
    print("num:",num)
except(ValueError,TypeError):
    print("not a valid integer")

try:
    f=open(r"day.txt","r")
    print(f.read())
except IOError:
    print("Wrong path")'''

'''try:
    num=int(input("Enter an integer number:"))
    print("Number:",num)
except(ValueError,TypeError):
    print("Not a valid integer")

a=input("Enter The Number:")
try:
    b=int(a)
    print(a,"is valid integer")
except ValueError:
    print("please Enter a Valid integer")'''

try:
    f=open("days.txt")
except FileNotFoundError:
    print('File not found')
print(f.read())
