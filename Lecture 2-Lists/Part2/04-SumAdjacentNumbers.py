

user_input = [float(a) for a in input().split()]
new_list = []
for item in user_input:
    while new_list and (item == new_list[-1]):
        new_list.pop()
        item *= 2
    new_list.append(item)

print(*new_list)


### Second solution sys while:
nums_list = list(map(float, input().split()))
length = len(nums_list) - 1
index = 0

while index < len(nums_list) - 1:
    if nums_list[index] == nums_list[index + 1]:
        current_sum = nums_list[index] + nums_list[index + 1]
        del nums_list[index + 1]
        nums_list[index] = current_sum
        index = -1
    index += 1

print(*nums_list)