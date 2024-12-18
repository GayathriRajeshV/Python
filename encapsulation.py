class Employee:
    def __init__(self, name, project):
        self.project = project
        self.name = name
    def work (self):
        print (self.name, 'is working on', self.project)
emp=Employee('Maya','Axis Bank')
emp.work()
