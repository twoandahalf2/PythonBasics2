##zadacha2 part 1 CountReal

user_input = list(map(float, input().split()))
#user_input = [8, 2.5, 2.5, 8, 2.5]

my_dict = {}

for num in user_input:
    counter = user_input.count(num)
    my_dict[num] = counter

my_dict_sorted = sorted(my_dict.items())

for item in my_dict_sorted:
    print(f'{item[0]} -> {item[1]} times')