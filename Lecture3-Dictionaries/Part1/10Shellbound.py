import math

user_input = input().split()

shells_dict = {}


while user_input[0] != 'Aggregate':
    location = user_input[0]
    location_item = int(user_input[1])
    if location in shells_dict.keys():
        if location_item not in shells_dict[location]:
            shells_dict[location].append(location_item)
        else:
            pass
    else:
        shells_dict[location] = []
        shells_dict[location].append(location_item)
    user_input = input().split()

for key,value in shells_dict.items():
    print(f'{key} -> ', end='')
    # for item in value:
    #     item = str(item)
    #     print(", ".join(item), end='') ####NOT WORKING SOMEHOW??????
    listty = ', '.join([str(x) for x in value])  ###Print comma separated list items that are INTs
    print(listty, end=' ')
    shell_sum = sum(value)
    shell_count = len(value)
    aggregate = (shell_sum - (shell_sum/shell_count))
    print(f'({math.ceil(aggregate)})')

