

my_dict = {}
user_input = input().split(' = ')

while user_input[0] != 'end':
    try:
        value = int(user_input[1])
        key = user_input[0]
        my_dict[key] = value
    except ValueError:
        if user_input[1] in my_dict.keys():
            my_dict[user_input[0]] = my_dict[user_input[1]]
    user_input = input().split(' = ')

for key,value in my_dict.items():
    print(f'{key} === {value}')