
#Exercise Question 4: Unpack the following tuple into 4 variables

tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1

print(a)
print(b)
print(c)
print(d)

#Exercise Question 5: Swap the following two tuples

tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(f't2 : {tuple2}')
print(f't1 : {tuple1}')

#Exercise Question 7: Modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)

