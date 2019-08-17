user_input = input().split(' : ')

results = {}

while user_input[0] != 'Over':
    if user_input[1].isdigit():
        key = user_input[0]
        value = user_input[1]
    else:
        key = user_input[1]
        value = user_input[0]

    results[key] = value

    user_input = input().split(' : ')


for k,v in sorted(results.items()):
    print(f'{k} -> {v}')