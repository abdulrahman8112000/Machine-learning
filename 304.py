user_name=input("Enter your user name")
password=input("Enter your password")

length=len(password)
password='*'*len(password)
print(f'Hey {user_name}, your password {password} is {length} characters long')