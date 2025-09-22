#  Repetition Algorithm (Calculate Total Grocery Bill for Multiple Items)
total = 0
print("if item price is 0 then you can print the amount")
item_price= float(input("enter item price:"))
while item_price!=0:
    total += item_price
    item_price= float(input("enter item price:"))
print("total is:",total)
