score=[]
name=[]
temp_dict={}
student1 = [{'id' : 'Std_1', 'name': 'Som', 'math': 35, 'science': 60},
            {'id' : 'Std_2', 'name': 'Vanitha', 'math': 15, 'science': 98},
            {'id' : 'Std_3', 'name': 'Divya', 'math': 100, 'science': 83}
            ]

sub = input('Enter Subject to find max score \n')

for i in student1:
    temp_dict.update({i['name'] : i[sub]})

#temp_dict = dict(zip(name, score))

print(temp_dict)

max_name = max(temp_dict, key = temp_dict.get)
min_name = min(temp_dict, key = temp_dict.get)

print(f'{max_name} scored highest in {sub} and the score : {temp_dict[max_name]} \n')
print(f'{min_name} scored lowest in {sub} and the score : {temp_dict[min_name]} \n')


