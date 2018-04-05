import random

lst = [random.randint(1, 9) for num in range(10)]
print (lst)
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)
# def change_min_max(lst):
#     max_num = 0
#     min_num = 10
#     res = 0
#     for  num in lst:
#         if num > max_num:
#             max_num = num

#         if num < min_num:
#             min_num = num
    
   

        
#     return print(min_num, max_num)
# 
lst[lst.index(max(lst))], lst[lst.index(min(lst))] = lst[lst.index(min(lst))], lst[lst.index(max(lst))]
print(lst)