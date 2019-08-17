
user_input = input().split(' -> ')
result = {}

while user_input[0] != 'login':
    key = user_input[0]
    value = user_input[1]
    result[key] = value
    user_input = input().split(' -> ')

user_input2 = input().split(' -> ')

counter = 0
while user_input2[0] != 'end':
    key_tocheck= user_input2[0]
    value_tocheck= user_input2[1]
    if key_tocheck in result.keys():
        if value_tocheck == result[key_tocheck]:
            print(f'{key_tocheck}: logged in successfully')
        else:
            print(f'{key_tocheck}: login failed')
            counter +=1
    else:
        print(f'{key_tocheck}: login failed')
        counter += 1
    user_input2 = input().split(' -> ')

print(f'unsuccessful login attempts: {counter}')