
user_input = input().split(':')

city_dict = {}

while user_input[0] != 'ready':
    city = user_input[0]
    if city not in city_dict.keys():
        city_dict[city] = {}
    capacity = user_input[1].split(',')
    for item in capacity:
        element = item.split('-')
        city_dict[city][element[0]] = element[1]
    user_input = input().split(':')

user_input2 = input().split()

while user_input2[0] != 'travel':
    city2 = user_input2[0]
    city_visitors = int(user_input2[1])
    for k,v in city_dict.items():
        if k == city2:
            total_value = 0
            for key,value in v.items():
                total_value += int(value)
            if city_visitors > total_value:
                print(f'{city2} -> all except {city_visitors- total_value} accommodated')
            else:
                print(f'{city2} -> all {city_visitors} accommodated')
    user_input2 = input().split()