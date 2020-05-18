#Exercise Question 1: Given a Python list you should be able to display Python list in the following order
#My logic
list1 = [100, 200, 300, 400, 500]
list2=[]
n = (len(list1)-1)
print(n)
while n >= 0 :
    list2.append(list1[n])
    n-=1
print(list2)

#Answer
list1 = [100, 200, 300, 400, 500]
list2 = list1[::-1]
print(list2)