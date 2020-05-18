#Exercise Question 4: Concatenate two lists in the following order

#my logic
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
i=0
for a in list1:
    j=0
    for b in list2:
        list3.append((list1[i]+list2[j]))
        j+=1
    i+=1
print(list3)

#answer
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

resList = [x+y for x in list1 for y in list2]
print(resList)
