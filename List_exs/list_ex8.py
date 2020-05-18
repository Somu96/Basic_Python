#Exercise Question 9: Given a Python list, find value 20 in the list, and if it is present,
# replace it with 200. Only update the first occurrence of a value
#my logic

list1 = [5, 10, 15, 20, 25, 50, 20, 80, 20]
i=0
for a in list1:
    if a == 20 :
        list1[i]=200
        break
    i+=1
print(list1)

#answer
list1 = [5, 10, 15, 20, 25, 50, 20, 80, 20]

index = list1.index(20)
list1[index] = 200
print(list1)