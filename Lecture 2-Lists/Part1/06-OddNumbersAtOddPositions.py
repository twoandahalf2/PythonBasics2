user_input = [int(a) for a in input().split(' ')]

counter = 0

for index, item in enumerate(user_input):
    if item % 2 == 1 or item % 2 == -1:
        if index % 2 != 0:
            print(f'Index {index} -> {item}')


