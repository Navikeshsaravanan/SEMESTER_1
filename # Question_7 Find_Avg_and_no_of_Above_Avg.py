# Question_7 Find_Avg_and_no_of_Above_Avg
import array as arr
a = arr.array('i',[1,2,3,4,5,6,7,8,9,10])
sum = 0
for i in range(0,len(a)):
    sum+=a[i]
avg=sum/len(a)
count = 0
for i in range(0,len(a)):
    if a[i]>avg:
        count+=1
print("The average of a array is :",avg)
print("The count above average is:",count)