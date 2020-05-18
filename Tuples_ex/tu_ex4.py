#Exercise Question 10: Check if all items in the following tuple are the same

def check_tu(tuple1):
    return all(i == tuple1[0] for i in tuple1)
tuple1 = (45, 45, 45, 45, 90/2)
print(check_tu(tuple1))