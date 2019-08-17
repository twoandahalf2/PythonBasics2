#shellbound

import math

vladi_input = input().split()
result = {}

while vladi_input[0] != 'Aggregate':
    key = vladi_input[0]
    value = vladi_input[1]
    for k, v in result.items():
        if key in k:
            if value not in v:
                v.append(value)
                break
            break
    else:
        result[key] = list()
        result[key].append(value)
    vladi_input = input().split()


for key,value in result.items():
    int_value = [int(x) for x in value]
    sum_of_shells = sum(int_value)
    count_of_shells = len(value)
    giant_shell = sum_of_shells - (sum_of_shells / count_of_shells)
    print(f'{key} -> ', end='')
    print(', '.join(value), end='')
    print(f' ({math.ceil(giant_shell):.0f})')

