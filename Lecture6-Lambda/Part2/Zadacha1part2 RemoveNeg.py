
###zadacha 1 part 2 Remove Negatives and Reverse

user_input = list(map(int, input().split(' ')))

##List comprehension
my_list = [n for n in user_input if n >= 0]

##Filter

# filter_list = list(filter(lambda n: n >= 0, my_list))
# print(filter_list)

my_list2 = my_list[::-1]
if my_list2:
    for i in my_list2:
        print(f'{i}', end=' ')
else:
    print('empty')