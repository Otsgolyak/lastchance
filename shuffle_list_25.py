import random


lst = []
for num in range(100):
    if num % 2 != 0:
        lst.append(num)
print(lst)                  
def shuffle_list(lst):
    empty_list = []
    count = 0
    while len(empty_list) != len(lst):
        for item in lst:
            item = random.choice(lst)
            if item not in empty_list:
                empty_list.append(item)
                count += 1
    return empty_list

           
        
    # for item in lst:
    #     rand_index = random.randint(0, len(empty_list)) 
    #     empty_list.insert((rand_index), item)
    #     return empty_list
print(shuffle_list(lst))
