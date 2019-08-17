n = int(input())

wardrobe = {}
items = []

while n > 0:
    items = []
    n -=1
    user_input = input().split(' -> ')
    key = user_input[0]
    values = user_input[1].split(',')
    if key not in wardrobe.keys():
        wardrobe[key] = values
    else:
        wardrobe[key] += values


user_input3 = input().split(' ', 1)
key_to_search=user_input3[0]
value_to_search=user_input3[1]


for key, value in wardrobe.items():
    print(f'{key} clothes:')
    repeatables = []
    for item in value:
        if value.count(item) > 1:
            if item in repeatables:
                continue
            else:
                if key == key_to_search and item == value_to_search:
                    print(f'* {item} - {value.count(item)} (found!)')
                    repeatables.append(item)
                else:
                    print(f'* {item} - {value.count(item)}')
                    repeatables.append(item)
                continue
        if key == key_to_search and item == value_to_search:
            print(f'* {item} - {value.count(item)} (found!)')
        else:
            print(f'* {item} - {value.count(item)}')