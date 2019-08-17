# nums_list = list(map(int, input().split()))
#
# positive_nums_list = list(filter(lambda num_vladi: num_vladi > 0, nums_list))
#
#
# if len(positive_nums_list) == 0:
#     print('empty')
#     exit(0)
# else:
#     print(*positive_nums_list[::-1])
#
# ## list comprehension !!!_


### zadacha 2
#
# nums_list = map(lambda num: float(num), input().split())

# hardcoded:
# nums_list = [3, 3, 6, 1]
# index = 0
#
# while index < len(nums_list) - 1:
#     if nums_list[index] == nums_list[index + 1]:
#         current_sum = nums_list[index] + nums_list[index + 1]
#         del nums_list[index]
#         nums_list[index] = current_sum
#         index = -1
#     index += 1
# print(*nums_list)


# ### zadacha 3 Wardrobe
#
# # zip function returns tuples
#
#
# n = int(input())
#
# wardrobe_dict = {}
#
# for iteration in range(n):
#     data_list = input().split(' -> ')
#     color = data_list[0]
#     clothes = data_list[1].split(',')
#     if color not in wardrobe_dict.keys():
#         wardrobe_dict[color] = []
#     wardrobe_dict[color].extend(clothes)
#
# # print(wardrobe_dict)
#
# items_count_dict = {}
#
# for color, clothes_list in wardrobe_dict.items():
#     items_count_dict[color] = {c: clothes_list.count(c) for c in clothes_list}
#
#
# color_to_be_found, clothes_to_be_found = input().split()
#
#
# for color, kvp in items_count_dict.items():
#     print(f'{color} clothes: ')
#     for c , c_count in kvp.items():
#         if color_to_be_found == color and clothes_to_be_found == c:
#             print(f'* {c} - {c_count} (found!)')
#         else:
#             print(f'* {c} - {c_count}')


### zadacha Dict - advanced

# data_list = input().split(' -> ')
# names_dict = {}
#
# while not data_list[0] == 'end':
#     name = data_list[0]
#     item = data_list[1].split(', ')
#
#     if len(item) > 1 and data_list[0].isdigit():
#         if name not in names_dict.keys():
#             names_dict = []
#         names_dict[name].extend(item)
#     else:
#         if item[0] in names_dict.keys():
#             if name not in names_dict.keys():
#                 names_dict[name] = []
#             names_dict[name].extend(names_dict[item[0]])


### zadacha Social media posts:








