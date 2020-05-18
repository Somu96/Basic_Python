#student nested dictionary


student = {'Std_1': {'name': 'Som', 'math': 35, 'science': 35},
           'Std_2': {'name': 'Vanitha', 'math': 99, 'science': 99}
           'Std_3': {'name': 'Divya', 'math': 100, 'science': 100}
           }
add_std = True
def get_stu_info():
    stu_id = input('Enter the ID for student \n')
    if stu_id in student.keys():
        print('Duplicate Student ID. Re-run the program')
    else:
        student[stu_id]={'name': input(f'Enter name for {stu_id} : '), 'math':input('Enter Math score : '), 'science':input('Enter Science Score : ')}

print("Welcome to Student records")

while add_std :
    add_std_check = input('Are you here add information of a student ? Yes/No \n')
    if add_std_check == 'Yes':
        get_stu_info()
    else:
        add_std = False
        print(f'Thank you here are the student details we have {student}')



