user_input = [int(a) for a in input().split()]
n = int(input())
user_input.sort(reverse=True)


for item in user_input:
    if n < 1:
        break
    else:
        print(item, end=' ')
        n -= 1
