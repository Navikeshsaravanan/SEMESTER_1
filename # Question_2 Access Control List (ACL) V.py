# Question_2 Access Control List (ACL) Validator
def identify_intruders(login_attempts, authorized_users):
    fl = []
    for i in login_attempts:
        if i not in authorized_users:
            fl.append(i)
    f_set = set(fl)
    print(f_set)
attempts = eval(input("enter the login_atempts in lists:"))
authorized = eval(input("enter the authorized_users in set"))
identify_intruders(attempts,authorized)