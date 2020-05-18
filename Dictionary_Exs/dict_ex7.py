# dictionary exercise 9: Get the key corresponding to the minimum value from the following dictionary
'''sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75,
  'som' : 10
}
print(min(sampleDict, key = sampleDict.get))'''

my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print(key_max)
print(key_min)
print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])