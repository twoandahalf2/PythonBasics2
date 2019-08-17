user_input = input()
result = {}

for item in user_input:
    if item not in result:
        result[item] = user_input.count(item)

for k, v in result.items():
    print(f'{k} -> {v}')