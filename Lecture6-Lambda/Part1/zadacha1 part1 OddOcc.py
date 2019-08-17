#zadacha 1 part 1

#zadacha 1

user_input = input().lower().split()

my_dict = {}

for item in user_input:
    my_dict[item] = user_input.count(item)

glist = []

for key,value in my_dict.items():
    if value % 2 != 0:
        glist.append(key)

print(*glist, sep=', ')

