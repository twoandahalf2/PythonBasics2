user_input = input()
result = {}
person = 1
while True:
    user_input=user_input.split()
    if user_input[0] == 'make':
        break
    else:
        pass
    counter = 0
    first_name = user_input[4]
    for letter in first_name:
        if letter == letter.upper():
            first_name = user_input[4]
            counter += 1
            break
        else:
            first_name = 'not valid'
            break
    last_name = user_input[5]
    for letter in last_name:
        if letter == letter.upper():
            last_name = user_input[5]
            counter +=1
            break
        else:
            last_name = 'not valid'
            break

    age = int(user_input[8])
    if 9 < age < 100:
        age = user_input[8]
        counter +=1
    else:
        pass
    date = user_input[14]
    try:
        date2 = date.split('-')
        if len(date2) == 3:
            counter+= 1
    except:
        pass
    if counter == 4:
        result[f'{person}'] = {'Name of the person': f'{first_name} {last_name}',
                               'Age of the person': f'{age}.', 'Birthdate of the person': date}
    user_input = input()
    person +=1

for key, value in result.items():
    for k,v in value.items():
        print(f'{k}: {v}')

if result == {}:
    print('DB is empty')
