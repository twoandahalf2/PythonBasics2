
user_input = input().split(':')

result = {}

while user_input[0] != 'ready':
    key = user_input[0]
    value_items = user_input[1]
    value_items = value_items.split(',')
    if key not in result.keys():
        result[key] = {}
    for item in value_items:
        nested_k, nested_v = item.split('-')
        result[key][nested_k] = nested_v
    user_input = input().split(':')

user_input = input().split()
result2 = {}

while user_input[0] != 'travel':
    number = int(user_input[1])
    city = user_input[0]
    for key, value in result.items():
        sum_total = 0
        if city == key:
            for k, v in value.items():
                sum_total += int(v)
            if sum_total > int(number):
                print(f'{city} -> all {number} accommodated')
            elif sum_total < number:
                print(f'{city} -> all except {number -sum_total} accommodated')
        else:

    user_input = input().split()