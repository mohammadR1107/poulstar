name = input("enter your name")
lastname = input("enter your last name")
age = int(input("enter your age"))
email = input("enter your email")
if not(email.endswith("@gmail.com")):
    print("invalid email address")
    print("try later")