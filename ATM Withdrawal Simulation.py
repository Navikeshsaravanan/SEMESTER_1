#Nested Condition with Loop (ATM Withdrawal Simulation)
'''cus_no = 1
while True:
    print("Enter the Customer ",cus_no," Details")
    balance = float(input("balance:"))
    withdrawal=float(input("enter withdrawal amount:"))
    if withdrawal < balance:
        balance -= withdrawal
        print("withdrawal sucessful,remaining balance:",balance)
    else:
        print("insufficient balance")
    ch = input("enter n to exit Transaction:")
    if ch.lower()=="n":
        print("thankyou")
        break
    print("Final balance:",balance)
'''
cus_no = int(input("no of customers:"))
for i in range(1,cus_no+1):
    print("Enter the Customer ",i," Details")
    balance = float(input("balance:"))
    withdrawal=float(input("withdrawal amount:"))
    if withdrawal <= balance:
        balance -= withdrawal
        print("withdrawal sucessful\nremaining balance:",balance,)
    else:
        req = withdrawal-balance
        print("insufficient balance and requried",req,"to withdraw the given amount")
print("Thankyou")