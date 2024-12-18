#21/11/2024
#Q1.)Write  a function to reverse a list without using the built in reverse() method.
'''def rev_lst(l):
    return l[::-l]
l=[98,87,45,78]
print("the reverse is",rev_lst(l))

#Q2.)Program to find second largest number in a list
l2=[89,67,54,65,89,78]

remove_dup=(list(set(12)))
print("The final list is",remove_dup)

sorted_list=sorted(remove_dup)
print("The sorted list is",sorted_list)

print("The second largest numbers in sorted list is",sorted_list[-2])

    
#Q3.)Program to do intersection of two lists
lA=[1,2,8,15,65,3,78]
lB=[1,8,52,3,45,65]
intersection=list(set(lA)&set(lB))
print(intersection)'''

#Q4.)find maximum and minimum from the list
number = [3, 5, 1, 8, 2, 9, 4]

# Finding maximum and minimum
print("Maximum:",max(number))
print("Minimum:",min(number))

#Q5.)Program to add and remove the elements from the list
my_list = [10, 20, 30, 40]

# Adding elements
my_list.append(50)  # Adds 50 at the end
my_list.insert(2, 25)  # Inserts 25 at index 2

# Removing elements
my_list.remove(20)  # Removes the first occurrence of 20
removed_element = my_list.pop(3)  # Removes element at index 3

print(f"List after modifications: {my_list}")
print(f"Removed element: {removed_element}")

#Q6.)Program to check whether the list is palindrome or not
def is_palindrome(lst):
    return lst == lst[::-1]

# Example usage
my_list = [1, 2, 3, 2, 1]
if is_palindrome(my_list):
    print("The list is a palindrome.")  # Output: The list is a palindrome.
else:
    print("The list is not a palindrome.")


   ''' Q.1)Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.

Q.2)WAP to reverse the element in List 

Q.3)WAP to find second smallest element in the list

Q.4) Perform Intersection operation on list'''
