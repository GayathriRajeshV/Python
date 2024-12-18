Number = int(input("Enter the Fibonacci Number Range = "))

A= 0
B = 1
Sum = 0

for Num in range(0, Number):
    print(A, end = '  ')
    Sum = Sum + A
    Next=A+B
    A=B
    B= Next

print("\nThe Sum of Fibonacci Series Numbers = %d" %Sum)
