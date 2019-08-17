

user_input = input().split(' -> ')
data_dict = {}


while user_input[0] != 'login':
    key = user_input[0]
    value = user_input[1]
    data_dict[key] = value
    user_input = input().split(' -> ')


login_attempt = input().split(' -> ')

failure = 0

while login_attempt[0] != 'end':
    if login_attempt[0] in data_dict.keys():
        if data_dict[login_attempt[0]] == login_attempt[1]:
            print(f'{login_attempt[0]}: logged in successfully')
        else:
            print(f'{login_attempt[0]}: login failed')
            failure += 1
    else:
        print(f'{login_attempt[0]}: login failed')
        failure += 1
    login_attempt = input().split(' -> ')
print(f'unsuccessful login attempts: {failure}')