input_key = input()
input_value = input()
n= int(input())

result = {}

for i in range(n):
    user_input = input().split(' => ')
    k= user_input[0]
    v= user_input[1]
    list_value = v.split(';')
    if input_key in k:
        print(f'{k}:')
        for item in list_value:
            if input_value in item:
                print(f'-{item}')