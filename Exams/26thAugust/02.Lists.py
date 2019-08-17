user_input = input().split()

result = []
list_type = None

while True:
    if user_input[0] == 'stop':
        break
    user_input = [int(x) for x in user_input]
    counter= 0
    for item in user_input:
        if user_input.count(item) > 1:
            counter += 1
    if counter == 0:
        list_type = 'unique'
    else:
        list_type = 'non-unique'
    if list_type == 'unique':
        for item in user_input:
            if item % 2 == 0:
                result.append(item + 2)
            else:
                result.append(item)
    elif list_type == 'non-unique':
        for item in user_input:
            if item % 2 != 0:
                result.append(item + 3)
            else:
                result.append(item)
    result = sorted(result)
    output = sum(result) / len(result)
    if list_type == 'unique':
        print(f'Unique list:', end=' ')
        print(','.join(map(str, result)))
    else:
        print(f'Non-unique list:', end=' ')
        print(':'.join(map(str, result)))
    print(f'Output: {output:.2f}')
    user_input = input().split()
    result = []
