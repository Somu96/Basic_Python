#dictionary exercise 10: Given a Python dictionary, Change Brad’s salary to 8500

sampledict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampledict['emp3']['salary']=8500
print(sampledict)