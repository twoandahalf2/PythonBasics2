## Zadacha 2 part2 TravelC

#input = Sofia:bus-30,airplane-150,train-25


user_input = input().split(':')

primary_dict = {}
secondary_dict = {}
values_list = []

while True:
    if user_input[0] == 'travel time!':
        print('travel time!')
        break
    values_list = user_input[1].split(',')
    for item in values_list:
        kvp = item.split('-')
        secondary_dict[kvp[0]] = int(kvp[1])
    primary_dict[user_input[0]] = secondary_dict.copy()
    user_input = input().split(':')


#print(secondary_dict)
print(primary_dict)
