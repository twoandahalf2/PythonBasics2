user_input = [int(a) for a in input().split()]

user_input.sort()

for item in user_input:
    print(item, end=' ')