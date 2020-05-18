#Exercise Question 1: Add a list of elements to a given set
set1={"Yellow", "Orange", "Black"}
l1=["Blue", "Green", "Red", 'Black', 'Black']

set1.update(l1)
print(set1)

#Exercise Question 2: Return a set of identical items from a given two Python set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3=(set1.intersection(set2))
print(set3)

#Exercise Question 3: Returns a new set with all items from both sets by removing duplicates
set3=set1.union(set2)
print(set3)

#Exercise Question 4: Given two Python sets,
# update first set with items that exist only in the first set and not in the second set.

set1.difference_update(set2)
print(set1)

#Exercise Question 5: Remove 10, 20, 30 elements from a following set at once
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)