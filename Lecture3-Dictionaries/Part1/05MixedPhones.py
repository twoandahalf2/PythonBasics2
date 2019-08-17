

book = {}
user_input = input().split(' : ')

while user_input[0] != 'Over':

    if user_input[1].isdigit():
        value = user_input[1]
        key = user_input[0]
        book[key] = value
    else:
        value = user_input[0]
        key = user_input[1]
        book[key] = value
    user_input = input().split(' : ')

for key,value in sorted(book.items()):
    print(f'{key} -> {value}')
