'''class Dog:
    def __init__(self,breed,color,name):
        self.b=breed
        self.c=color
        self.n=name
d=Dog("Pomerian","White","Fluffy")
print(d.n)
print(d.c)
print(d.b)
print(d.b ,d.c ,d.n)

class Complex:
    def __init__(self,real,imaginary):
        self.r=real
        self.i=imaginary
c=Complex(11,22)
print(c.i, c.r)'''

class Dog:
    tricks=[]
    def __init__(self,name):
        self.n=name
        
    def add_trick(self,trick):
        self.trick.append(tricks)
        
d=Dog("Buddy")
e=Dog("Fido")
d.add_tricks("Play dead")
e.add_tricks("Shake hand")

