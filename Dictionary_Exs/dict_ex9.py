#Student Netst dictionary
'''dict = {'stu_1' : {'name': 'Som', 'math': 90, 'science': 95},
        'stu_2' : {'name': 'Som1', 'math': 80, 'science': 85},
        'stu_3' : {'name': 'Som2', 'math': 85, 'science': 75},
        'stu_4' : {'name': 'Som3', 'math': 87, 'science': 65}
        }'''
dict = { }

def student():
    sid = input('Enter Student ID \n')
    if sid in dict.keys():
        print('Duplicate Student ID')
    else:
        dict[sid]= {'name': input(f'Enter name for {sid} : '), 'math':input('Enter Math score : '), 'science':input('Enter Science Score : ')}
a = input('Looking to feed student inforation? Yes/No \n ')
if a == 'Yes':
    student()
else :
    print('Thank you visit again')
print(dict)





