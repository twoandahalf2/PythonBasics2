user_input = input().split(' -> ')
result = {}

while user_input[0] != 'filter':
    topic = user_input[0]
    values_list = user_input[1].split(', ')
    # values_list = [x for x in values_list]
    if topic in result.keys():
        result[topic] += values_list
    else:
        result[topic] = values_list
    user_input = input().split(' -> ')

user_input2 = input().split(', ')
n = len(user_input2)

for key, value in result.items():
    value = list(dict.fromkeys(value))
    counter = 0
    for item in user_input2:
        if item in value:
            counter +=1
        if counter == n:
            # print(f"{key} | #{', #'.join(value)}")  ####PRINT PREPHIX
            # counter = 0
            a = ", "
            b = "#"
            val_list = [b + val for val in value]
            print(f"{key} | {a.join(val_list)}")
