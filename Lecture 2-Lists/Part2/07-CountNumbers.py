user_input = [int(a) for a in input().split()]

result = sorted(user_input)

count =1
length = len(result) -1
index = 0

while index <= length:
    if index == length:
        print(f'{result[index]} -> {count}')
    elif result[index] == result[index + 1]:
        count +=1
    else:
        print(f'{result[index]} -> {count}')
        count = 1
    index +=1
