
user_input = input().split(' -> ')

result = {}

while user_input[0] != 'end':
    name = user_input[0]
    try:
        values_list = user_input[1].split(', ')
        values_list = [int(x) for x in values_list]
        if name in result.keys():
            result[name] += values_list
        else:
            result[name] = values_list
    except ValueError:
        value = user_input[1]
        if value in result.keys():
            result[name] = result[value].copy()
        else:
            pass
    user_input = input().split(' -> ')

for k, v in result.items():
    print(f'{k} === ',end='')
    print(*v, sep=", ")

# a = [1, 2, 3, 4, 5]
# print(' '.join(map(str, a)))
#
#

