#dictionary exercise 5: Create a new dictionary by extracting the following keys from a given dictionary

sampledict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ['name','salary']
dict1 = {k:sampledict[k] for k in keys}
print(dict1)
