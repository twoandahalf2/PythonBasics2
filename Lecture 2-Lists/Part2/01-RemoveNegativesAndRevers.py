user_input = [int(a) for a in input().split(' ') if int(a) > 0]

result = reversed(user_input)

if not user_input:
    print('empty')
else:
    print(*result)
