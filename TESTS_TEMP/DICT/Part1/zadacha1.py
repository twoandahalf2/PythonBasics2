user_input = input().split()
new_list = []
result = []
for item in user_input:
    new_list.append(item.lower())

for el in new_list:
    if (new_list.count(el) % 2 != 0) and el not in result:
        result.append(el)
print(', '.join(result))