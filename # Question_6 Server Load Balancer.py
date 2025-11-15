# Question_6 Server Load Balancer
def distribute_tasks(server_loads,new_tasks):
    mini = server_loads[0]
    for i in range(new_tasks):
        for j in server_loads:
            if j <mini:
                server_loads.insert(server_loads.index(j),j+1)
                server_loads.remove(j)
                mini = j
    print(server_loads)
serverload = eval(input("enter the server loads in lists:"))
newtask = int(input("enter the new task:"))
distribute_tasks(serverload,newtask)