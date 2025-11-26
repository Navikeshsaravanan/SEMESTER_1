#Question_3 find count of even and odd numbers
import array as arr
a = arr.array('i',[1,2,3])
ecount=ocount=0
for i in range(0,len(a)):
    if a[i]%2 == 0:
        ecount+=1
    elif a[i] %2 != 0:
        ocount+=1
print("the no of odd number is:",ocount)
print("the no of even number is:",ecount)