###zadacha 6 part1 ExamShopping



user_input = input().split()

supply_dict = {}

while True:
    if user_input[0] == 'shopping':
        break
    else:
        key = user_input[1]
        value = int(user_input[2])
        if key in supply_dict.keys():
            supply_dict[key] += int(value)
        else:
            supply_dict[key] = int(value)
        user_input = input().split()

###Dict ready , now substract:

user_input = input().split()

while True:
    if user_input[0] == 'exam':
        break
    key = user_input[1]
    value = int(user_input[2])
    if key in supply_dict.keys():
        if supply_dict[key] == 0:
            print(f'{user_input[1]} out of stock')
        supply_dict[key] -= int(value)
        if supply_dict[key] < 0:
            supply_dict[key] = 0
    else:
        print(f'{user_input[1]} doesn\'t exist')
    user_input = input().split()

for k, v in supply_dict.items():
    if v == 0:
        pass
    else:
        print(f'{k} -> {v}')

