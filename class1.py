class student:
    def _init_(self, roll, name, marks):
        self.roll=roll
        print("Roll No:",self.roll)
        self.name=name
        self.marks=marks
    def grade(self): 
        if(self.marks>=80):
            print(self.name,"You score A+")
        elif(self.marks>=70):
            print(self.name,"You score A")
        elif(self.marks>=60):
            print(self.name,"You score B")
        elif(self.marks>=50):
            print(self.name,"You score C")
        elif(self.marks>=40):
            print(self.name,"You score D")
        else:
            print(self.name,"You are fail")
s=student(1,"Ansh",73)
print(s.grade())
