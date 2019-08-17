user_input = [int(a) for a in input().split(' ')]

counter = 0

for item in user_input:
    if item % 2 == 1 or item % 2 == -1:
        counter+=1

print(counter)