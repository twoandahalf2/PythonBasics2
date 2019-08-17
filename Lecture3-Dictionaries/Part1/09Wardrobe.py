n = int(input())

wardrobe = {}

for i in range(n):
    user_input = input().split(' -> ')
    key = user_input[0]
    items = user_input[1].split(',')
    if key in wardrobe.keys():
        wardrobe[key] += items
    else:
        wardrobe[key] = items

search = input().split()
temp_list = []

for key,values_list in wardrobe.items():
    print(f'{key} clothes:')
    for item in values_list:
        if item in temp_list:
            continue
        elif values_list.count(item) > 1:
            temp_list.append(item)
            if search[0] == key and search[1] == item:
                print(f'* {item} - {values_list.count(item)} (found!)')
            else:
                print(f'* {item} - {values_list.count(item)}')
        elif values_list.count(item) <= 1:
            if search[0] == key and search[1] == item:
                print(f'* {item} - {values_list.count(item)} (found!)')
            else:
                print(f'* {item} - {values_list.count(item)}')
