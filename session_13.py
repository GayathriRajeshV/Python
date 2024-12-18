#25/11/24
#function is block of code for specific logic
'''def welcome():
    print("You are welcome")

welcome()

name="Gayathri"
id=89
def welcome():
    print("You are welcome",name)

welcome()

class userInfo:
    def putData(self):
        self.name=input("Enter your name ")
        self.id=int(input("Enter your id "))
        self.salary=float(input("Enter your salary "))
    def display(self):
        print("UserName:",self.name)
        print("User Id:",self.id)
        print("User Salary:",self.salary)

obj=userInfo()
obj.putData()
obj.display()'''

class Student:
    def __init__(self,name,age,grade):
    #initializes the student object.
    self.name=name
    self.age=age
    self.grade=grade

    def display_info(self):
        #Display the student's information
        print(f"Name:{self.name},Age:{self.age},Grade:{self.grade}")
        print("Nmae:",self.name."Age:",self.age)


#creating objects
student1 =Student("Alice",14,"9th")
student2 =Student("Bob",15,"10th")

#Accessing object methods
student1.display_info()
students.display_info()


#Program to print bookdata as title, year, author etc with class and object concept

