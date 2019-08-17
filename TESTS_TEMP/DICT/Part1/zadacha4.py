

user_input = input().split(' = ')
result = {}

while user_input[0] != 'end':
    key = user_input[0]
    value = user_input[1]
    if value.isdigit():
        result[key] = value
    elif value in result.keys():
        result[key] = result[value]
    user_input = input().split(' = ')

for k,v in result.items():
    print(f'{k} === {int(v)}')