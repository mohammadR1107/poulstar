age = int(input("enter your age: "))
if age < 13:
    print("child")
elif (age > 13) and (age<17):
    print("teenager")
elif (age>17) and (age<35):
    print("young")
elif (age>35) and (age<50):
    print("middle aged")
else:
    print("the old")