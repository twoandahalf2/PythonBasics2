# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# tuple_1 = ['History', 'Math', 'Physics', 'CompSci']
#
# cs_set = {'History', 'Math', 'Physics', 'CompSci'}  # order is always mixed and duplicates are removed!
#
# nums = [1,2,3,4,4,5,6,7,8,8,9,10]
#
# my_list = list(map(lambda n: n*n, nums))
#
#
# print(my_list)
#
# my_list2 = list(filter(lambda n: n%2 == 0, nums))
# my_list3 = set(filter(lambda n: n%2 == 0, nums))
# print(my_list2)
# print(my_list3)
# my_list3 = list(my_list3)
# print(type(my_list3))
#
####Dict comprehensions

# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = ['batman', 'Vladi', 'Gancho', 'Ivan']
#
# my_dict = {subject:lecturer for subject , lecturer in zip(list_1, list_2) if lecturer != 'Vladi'}
#
# print(my_dict)



# ####Set comprehensions
#
# nums = [1, 1, 2, 1, 3, 4,3,5, 5,6,7,8,9,9]
#
# my_set = {n for n in nums}
#
# print(my_set)

numbs1 = [4,3,2,1]
print(list(map(lambda x:x**2, numbs1)))
numbs2 = [4,3,2,1]
my_list = [n**2 for n in numbs2 if n % 2 ==0]
print(my_list)