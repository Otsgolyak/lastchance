# import random


# lst = []
# for num in range(100):
#     if num % 2 != 0:
#         lst.append(num)
# print(lst)                  
# def shuffle_list(lst):
#     empty_list = []
#     count = 0
#     while len(empty_list) != len(lst):
#         for item in lst:
#             item = random.choice(lst)
#             if item not in empty_list:
#                 empty_list.append(item)
#                 count += 1
#     return empty_list

import random
def shuffle_list ():
    lst = [i for i in range(1, 100) if i % 2 != 0]
    print(lst)
    print(id(lst))

    sequence_number = len(lst)
    while sequence_number > 1:
        sequence_number = sequence_number - 1
        rand_number = random.randint(0, sequence_number)
        lst[rand_number], lst[sequence_number] = lst[sequence_number], lst[rand_number]
    return lst, id(lst)
print(shuffle_list())

        
