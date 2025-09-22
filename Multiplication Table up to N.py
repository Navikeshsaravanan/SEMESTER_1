#Nested Loop (Print Multiplication Table up to N)
'''
n = int(input("enter number:"))
i = 1
j=1
while i <= n:
    j = 1
    while j <= 10:
        print( j,"*", i,"=",i*j)
        j+=1
    i+=1
'''
n = int(input("enter number:"))
for i in range(1,n+1):
    for j in range(1,11):
        print(j,"*",i,"=",i*j)