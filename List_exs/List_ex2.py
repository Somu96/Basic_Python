#Exercise Question 2: Concatenate two lists index-wise

#My Logic
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
i=0
for a in list1:
    list3.append((list1[i]+list2[i]))
    i+=1
print(list3)

#Answer
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)