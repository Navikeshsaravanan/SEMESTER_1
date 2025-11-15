# Question_7 Game Character Movement (List as Array)
def simulate_movement(size,moves):
    sum = 0
    for i in moves:
        sum +=i
        if sum<0:
            sum = 0
        elif sum >size:
            sum = size-1
    print(sum)
siz = int(input("enter the size:"))
movs= eval(input("enter the moves in list:"))
simulate_movement(siz,movs)