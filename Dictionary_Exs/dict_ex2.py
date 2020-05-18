#dictionary exercise 2: Merge following two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict2, **dict1}
print(dict3)

# dictionary exercise 3: Access the value of key ‘history’

sampledict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampledict)
print(sampledict['class']['student']['marks']['history'])
