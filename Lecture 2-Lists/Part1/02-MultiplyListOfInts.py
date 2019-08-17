user_input = [int(a) for a in input().split()]
p = int(input())

result = []

for i in user_input:
    i = i * p
    result.append(i)

print(*result)

