user_input = input()

count_of_letters = {}

for item in user_input:
    if item in count_of_letters:
        count_of_letters[item] += 1
    else:
        count_of_letters[item] = 1

for key,value in count_of_letters.items():
    print(f'{key} -> {value}')
    