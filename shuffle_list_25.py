import random

spisok = []
for i in range(100):
    if i % 2 != 0:
        spisok.append(i)
print(spisok)                  
def lol(spisok):
    empty_list = []
    count = len(spisok)
    scetchik = 0
    while len(empty_list) != len(spisok):
        for item in spisok:
            item = random.choice(spisok)
            if item not in empty_list:
                empty_list.append(item)
                scetchik += 1
    return empty_list

           
        
    # for item in spisok:
    #     rand_index = random.randint(0, len(empty_list)) 
    #     empty_list.insert((rand_index), item)
    #     return empty_list
print(lol(spisok))
