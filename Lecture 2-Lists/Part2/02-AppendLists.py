user_input = input().split('|')
result = []
counter = len(user_input) -1


while counter >= 0:
    a = user_input[counter].split()
    for item in a:
        result.append(item)
    counter -=1

print(*result)


