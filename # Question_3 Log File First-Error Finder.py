# Question_3  Log File First-Error Finder
def find_first_error(log_data):
    time= log_data[0][0]
    for  i in log_data:
        if i[1] == 'ERROR':
