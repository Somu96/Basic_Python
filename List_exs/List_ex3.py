#Exercise Question 3: Given a Python list. Turn every item of a list into its square root

#my logic
list1= [1, 2, 3, 4, 5, 6, 7]
list2 = []
for i in list1:
    list2.append((i*i))
print(list2)

#anser
aList = [1, 2, 3, 4, 5, 6, 7]
aList =  [x * x for x in aList]
print(aList)