class Student:
    marks = []
    def getData(self, rn, name, m1):
        Student.rn = rn
        Student.name = name
        Student.marks.append(m1)
        
    def displayData(self):
        print ("Roll Number is: ", Student.rn)
        print ("Name is: ", Student.name)
        print ("Marks are: ", Student.marks)
        
    def total(self):
        return (Student.marks[0] + Student.marks[1] +Student.marks[2])
    def average(self):
        return ((Student.marks[0] + Student.marks[1] +Student.marks[2])/3)
    
r = int (input("Enter the roll number: "))
name = input("Enter the name: ")
m1 = int (input("Enter the marks in the first subject: "))

s1 = Student()
s1.getData(r, name, m1, m2, m3)
s1.displayData()
