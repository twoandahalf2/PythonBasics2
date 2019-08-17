###zadacha3 part 1 SumAdjacent

#user_input = [3 ,3, 6,1]
user_input = list(map(int, input().split(' ')))

index = 0

while index < len(user_input) -1:
    if user_input[index] == user_input[index + 1]:
        current_sum = user_input[index] + user_input[index + 1]
        del user_input[index]
        user_input[index] = current_sum
        index = -1
    index += 1

print(*user_input)
