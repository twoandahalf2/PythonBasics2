#######Replace with correct CODE!


user_input = input().split()

supply_dict = {}


while user_input[0] != 'shopping':
    if user_input == ('exam time' and 'shopping time'):
        break
    key = user_input[1]
    value = int(user_input[2])
    if key in supply_dict:
        supply_dict[key] += value
    else:
        supply_dict[key] = value
    user_input = input().split()

user_input = input().split()

while user_input[0] != 'exam':
    if user_input == 'exam time':
        break
    key = user_input[1]
    value = int(user_input[2])
    if key in supply_dict:
        supply_dict[key] -= value
    else:
        print(f'{key} doesn\'t exist')
    user_input = input().split()


for key,value in supply_dict.items():
    if value == 0:
        continue
    elif value <0:
        print(f'{key} out of stock')
    else:
        print(f'{key} -> {value}')