count=int(input('Please enter the number of students:'))
f=open("marks.txt","w")
f.write('name, ')
f.write('marks, ')
f.write('rollno. \n')
for i in range(count):
    print('please enter the detail of ',i+1,' student:')
    name=input('Please enter the name:')
    marks=int(input('Please enter the marks:'))
    rollno=int(input('Please enter the rollno:'))
    details=name+',    '+str(marks)+ ',    '+str(rollno)+ '\n'
    f.write(details)
f.close()
