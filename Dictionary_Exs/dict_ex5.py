#dictionary exercise 6: Delete set of keys from Python Dictionary

sampledict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
n=25
print(n in sampledict.values())
keystoremove = ["name", "salary"]
sampledict = {k:sampledict[k] for k in sampledict.keys() - keystoremove}
print(sampledict)
