n=int(input("Enter the number:"))
flag = 0
for i in range(2,n+1):
  if n%i==0:
    flag = 1
    break
if flag == 1:
  print("Not Prime")
else:
  print("Prime")
