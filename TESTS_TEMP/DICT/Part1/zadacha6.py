

user_input = input().split()
supply = {}

while user_input[0] != 'shopping':
    key = user_input[1]
    value = int(user_input[2])
    if key in supply.keys():
        supply[key] += value
    else:
        supply[key] = value
    user_input = input().split()

user_input2 = input().split()

while user_input2[0] != 'exam':
    key = user_input2[1]
    value = int(user_input2[2])
    if key in supply.keys():
        if supply[key] <=0:
            print(f'{key} out of stock')
        elif value > supply[key]:
            supply[key] = 0
        else:
            supply[key] -= value
    else:
        print(f'{key} doesn\'t exist')
    user_input2 = input().split()

for k, v in supply.items():
    if v >0:
        print(f'{k} -> {v}')