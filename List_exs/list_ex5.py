#Exercise Question 5: Given a two Python list. Iterate both lists simultaneously such that
# list1 should display item in original order and list2 in reverse order

#My logic
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
n = (len(list2)-1)
for a in list1:
    print(a, list2[n])
    n-=1

#Answer
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)