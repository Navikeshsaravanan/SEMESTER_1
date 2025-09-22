# building a simple calculator
'''no = int(input("enter t=no of times to use:"))
ini = 0
while ini< no:
    number_1 = int(input("enter NO 1:"))
    number_2 = int(input("enter NO 2:"))
    choice = input("enter a operation + or - or * or /:")
    if choice == "+":
        result = number_1 + number_2
        print("you have chosen addition \n",result)
    elif choice == "-":
        result = number_1 - number_2
        print("you have chosen substraction \n",result)
    elif choice == "*":
        result = number_1*number_2
        print("you have chosen multiplication \n",result)
    elif choice == "/":
        result = number_1 / number_2
        print("you have chosen division \n",result)
    else:
        print("enter a valid operator")
    ini += 1
print("the program has ended ")
'''
no = int(input("enter no of times to use:"))
for i in range(no):
    number_1 = int(input("enter NO 1:"))
    number_2 = int(input("enter NO 2:"))
    choice = input("enter a operation + or - or * or /:")
    if choice == "+":
        result = number_1 + number_2
        print("you have chosen addition \n",result)
    elif choice == "-":
        result = number_1 - number_2
        print("you have chosen substraction \n",result)
    elif choice == "*":
        result = number_1*number_2
        print("you have chosen multiplication \n",result)
    elif choice == "/":
        result = number_1 / number_2
        print("you have chosen division \n",result)
    else:
        print("enter a valid operator")
print("the program has ended ")