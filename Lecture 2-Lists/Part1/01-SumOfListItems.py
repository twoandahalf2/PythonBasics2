n = int(input())

list_of_int = []

while n > 0:
    n -=1
    p = int(input())
    list_of_int.append(p)

print(sum(list_of_int))
