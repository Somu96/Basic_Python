#Exercise Question 8: Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

tuple1 = sorted(tuple1, key=lambda x: x[1])

print(tuple1)

#Exercise Question 9: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)
count = 0
for a in tuple1:
    if a == 50 :
        count+=1
print(count)

print(tuple1.count(50))