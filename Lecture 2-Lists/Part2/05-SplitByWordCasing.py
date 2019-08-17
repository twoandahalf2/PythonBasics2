# wardrobe - https://pastebin.com/ZSXep6DZ
# dict ref advanced - https://pastebin.com/9yhm9M89
# social media posts - https://pastebin.com/4GT5waec

a_list = input()
list_separators = [",", ";", ":", ".", "!", "(", ")", "\"", "\'", "\\", "/", "[", "]", " "]
for separator in list_separators:
    a_list = a_list.replace(separator, ' ')
print(a_list)
a_list = a_list.split()
print(a_list)
lower = []
mixed = []
upper = []

for word in a_list:
    if word.islower():
        if word.isalpha():
            lower.append(word)
        else:
            mixed.append(word)
    elif word.isupper():
        if word.isalpha():
            upper.append(word)
        else:
            mixed.append(word)
    else:
        mixed.append(word)

print(f"Lower-case: {' '.join(lower)}")
print(f"Mixed-case: {' '.join(mixed)}")
print(f"Upper-case: {' '.join(upper)}")