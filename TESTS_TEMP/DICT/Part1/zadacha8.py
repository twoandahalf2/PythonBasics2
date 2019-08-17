
user_input = input().split(' -> ')

age_dict = {}
salary_dict = {}
position_dict = {}


while user_input[0] != 'filter base':
    key = user_input[0]
    value = user_input[1]
    try:
        value = int(value)
        age_dict[key] = value
    except ValueError:
        try:
            value = float(value)
            salary_dict[key] = value
        except ValueError:
            position_dict[key] = value
    user_input = input().split(' -> ')

user_input2 = input()
if user_input2 == 'Position':
    for key, value in position_dict.items():
        print(f'Name: {key}')
        print(f'Position: {value}')
        print('====================')
elif user_input2 == 'Age':
    for key, value in age_dict.items():
        print(f'Name: {key}')
        print(f'Age: {value}')
        print('====================')
elif user_input2 == 'Salary':
    for key, value in salary_dict.items():
        print(f'Name: {key}')
        print(f'Salary: {value}')
        print('====================')