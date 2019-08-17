### zadacha 10 part 1 ShellBound

user_input = input().split(' ')

my_dict = {}
value_list= []

while True:
    if user_input[0] == 'Aggregate':
        break
    key = user_input[0]
    value = int(user_input[1])
    if key in my_dict.keys():
        if value not in my_dict[key]:
            my_dict[key].append(value)
    else:
        my_dict[key] = []
        my_dict[key].append(value)

    user_input = input().split(' ')


for key in my_dict.keys():
    sum_shells = sum(my_dict[key]) - (sum(my_dict[key]) // len(my_dict[key]))
    if len(my_dict[key]) == 1:
        print(f"{key} -> {', '.join(str(item) for item in my_dict[key])} ({my_dict[key][0]})")
    else:
        print(f"{key} -> {', '.join(str(item) for item in my_dict[key])} ({sum_shells})")

