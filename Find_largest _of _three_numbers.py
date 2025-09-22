#Selection Algorithm (Find largest of three numbers)
a,b,c = int(input("enter value 1 :")),int(input("enter value 2 :")),int(input("enter value 3 :"))
if a >b and a>c:
    largest = a
elif b>c:
    largest = b
else :
    largest = c
print("the laegest number in given numbers:",largest)
