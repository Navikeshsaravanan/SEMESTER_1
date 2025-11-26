# Question_2 largest and smallest elements in an array without max and min function
import array as arr
a = arr.array('i',[1,2,3])
maxi = 0
mini = a[1]
for i in range(0,len(a)):
    if a[i]>maxi:
        maxi = a[i]
    if a[i]<mini:
        mini = a[i]
print("the maximum value found in the array is:",maxi)
print("the minimum value found in the array is:",mini)