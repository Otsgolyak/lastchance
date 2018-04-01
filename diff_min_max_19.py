import random

def diff_min_max (num_limit, lower_bound, upper_bound):
    maximum_number = lower_bound
    minimum_number = upper_bound
    for _ in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print('random num: ', rand_num)
        if rand_num > maximum_number:
           maximum_number = rand_num
           print('max: ', maximum_number) 
        elif rand_num < minimum_number:
             minimum_number = rand_num 
        print('min: ', minimum_number)     
    return maximum_number - minimum_number
print("result: ", diff_min_max(12, 100, 250)) 