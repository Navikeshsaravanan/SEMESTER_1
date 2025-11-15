# Question_8 File System Organizer
def group_by_extension(files):
    lis = []
    f_dict = {}
    for i in files:
        h = i.split(".")
        lis.append(h[1])
        h.clear()
    for j in lis:
        
file = eval(input("enter the files in list:"))
group_by_extension(file)