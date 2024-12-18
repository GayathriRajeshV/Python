'''#Real time Example on Sets
sports1={"Sanoj","Neha","Dev","Raj","Shweta","Hiral"}
sports2={"Neha","Shweta","Hiral","Arjun","Ram","Sahyog"}

#Find total participants in the sports list
Total_Ath=sports1|sports2
print("Total players are",Total_Ath)

for i in Total_Ath:
    print(i)

#set difference
New_sports1=sports1-sports2
print("\nThe new sports onre list is:",New_sports1)'''

#Program to accept different email ids of customer(repeat atleast 3)in list and try print unique emails
email=["user@yahoo.com","gayu@gmail.com","user@yahoo.com","arj@gmail.com","Reem@gmail.come","user@yahoo.com"]
print("Enter email ids:")
print(email)

unique_email=set(email)
print("The unique datas are:",unique_email)

new_emails={"maya@gmail.com","harsh@gmail.come","arj@gmail.com","giri@yahoo.com"}
update=new_emails-unique_email
print(update)
    
