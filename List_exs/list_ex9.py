#Exercise Question 10: Given a Python list, remove all occurrence of 20 from the list

list1 = [5, 20, 15, 20, 25, 50, 20]

def removevalue(sampleList, val):
   return [value for value in sampleList if value != val]
resList = removevalue(list1, 20)
print(resList)