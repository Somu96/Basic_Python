#Exercise Question 6: Return a set of all elements in either A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = {10}
print(set1.symmetric_difference(set2))
#set3 = (set1.differnce_update(set2))
#set3.update(set2.difference_update(set1))
#print(set3)


#Exercise Question 7: Determines whether or not the following two sets have any elements in common.
# If yes display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1.intersection(set2))
