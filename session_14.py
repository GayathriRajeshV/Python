#26/11/24
#Exception
'''In Python, an exception is an event that occurs during the execution of a program, disruting its normal flow. Exceptions typically arise due to errors such as invalid input, division by zero, or accessing invalid indices in a list.
common Exceotion in python
1. ZeroDivisionError:
    Raised when dividing bu zero.
    print(10/0) #ZeroDivisionError

2. TypeError:
    Raised when an operation is applied to an object of an inappropriate type.
    print('10'+5)#Type error

3.ValueError:
    Raised when a function receives an arguement of the right type but an inaapropriate value
    int("abc") #ValueError

4.IndexError
    Raised when trying to access an index outside the range of a list
    lst=[1,2,3]
    print(lst[5])#indexError

5.KeyError:Raised when trying to access a non-existing key in a dictionary.
    d={"key":"value"}
    print(d["no key"])#KeyError
'''


