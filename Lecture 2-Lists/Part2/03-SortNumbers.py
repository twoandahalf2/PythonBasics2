###Ne moje da joinvame int !!!

user_input = [int(a) for a in input().split(' ')]
user_input.sort()
user_input = [str(a) for a in user_input]
print(' <= '.join(user_input))
