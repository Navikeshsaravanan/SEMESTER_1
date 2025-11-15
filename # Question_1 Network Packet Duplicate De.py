# Question_1 Network Packet Duplicate Detector
def find_duplicate_packets(a):
    ans = {}
    s = set(a)
    for i in s:
        if a.count(i) >1:
            ans[i] = a.count(i)
    print(ans)
lis = eval(input("enter the unique sequence number in list:"))
find_duplicate_packets(lis)