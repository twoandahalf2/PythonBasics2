user_input = [float(x) for x in input().split()]
user_input.sort()
counter= 0
result = {}
for item in user_input:
    if item not in result:
        result[item] = user_input.count(item)


for k, v in result.items():
    print(f'{k} -> {v} times')