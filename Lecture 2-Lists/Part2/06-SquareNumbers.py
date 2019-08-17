#### NEGATIVNITE SE RAZKARVAT

import math

user_input = [int(a) for a in input().split(' ')]
result = []

for item in user_input:
    if item < 0:
        continue
    elif math.sqrt(item).is_integer():
        result.append(item)

sorted_list = sorted(result, reverse=True)
print(*sorted_list)