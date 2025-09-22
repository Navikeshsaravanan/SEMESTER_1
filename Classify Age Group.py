# Nested Selection (Classify Age Group)
age = float (input("enter the age:"))
if age<18:
    if age <13:
        print("child")
    else:
        print("Teenager")
else:
    if age < 60 :
        print("Adult")
    else:
        print("senoir")

