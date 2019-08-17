user_input = [a for a in input().split()]


result = []

result.append(user_input[-1])
for item in user_input[0:-1]:
    result.append(item)

for item in result:
    print(item, end=' ')
